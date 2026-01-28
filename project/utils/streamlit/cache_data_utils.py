"""
Streamlit cache utilities for reusable cached functions.

This module provides cached functions that can be shared across different pages
and components to improve performance and avoid redundant processing.
"""

import streamlit as st
import pandas as pd
from io import BytesIO
from typing import Optional, Any, Callable
import hashlib


@st.cache_data(show_spinner="📖 Reading Excel file...")
def read_excel_cached(file_bytes: bytes, file_name: str, header: int = 0, 
                     sheet_name: int | str = 0) -> Optional[pd.DataFrame]:
    """Read Excel file with caching support.
    
    Args:
        file_bytes: File content as bytes
        file_name: Name of the file (for logging/display)
        header: Row number to use as header (default: 0)
        sheet_name: Sheet to read (default: 0)
        
    Returns:
        DataFrame or None if error
    """
    try:
        df = pd.read_excel(BytesIO(file_bytes), header=header, sheet_name=sheet_name)
        return df
    except Exception as e:
        st.error(f"❌ Error reading {file_name}: {e}")
        return None


@st.cache_data(show_spinner="📊 Processing data...")
def process_dataframe_cached(df: pd.DataFrame, 
                            process_func: Callable[[pd.DataFrame], pd.DataFrame],
                            cache_key: str) -> pd.DataFrame:
    """Process DataFrame with caching using a custom processing function.
    
    Args:
        df: Input DataFrame
        process_func: Function to process the DataFrame
        cache_key: Unique key for this processing operation
        
    Returns:
        Processed DataFrame
    """
    return process_func(df)


@st.cache_data
def convert_df_to_excel(df: pd.DataFrame, sheet_name: str = "Sheet1") -> bytes:
    """Convert DataFrame to Excel bytes with caching.
    
    Args:
        df: DataFrame to convert
        sheet_name: Name of the Excel sheet (default: "Sheet1")
        
    Returns:
        Excel file as bytes
    """
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
    buffer.seek(0)
    return buffer.getvalue()


@st.cache_data
def convert_df_to_csv(df: pd.DataFrame, sep: str = ',', encoding: str = 'utf-8') -> bytes:
    """Convert DataFrame to CSV bytes with caching.
    
    Args:
        df: DataFrame to convert
        sep: Column separator (default: ',')
        encoding: Text encoding (default: 'utf-8')
        
    Returns:
        CSV file as bytes
    """
    return df.to_csv(index=False, sep=sep, encoding=encoding).encode(encoding)


@st.cache_data(ttl=3600)
def compute_dataframe_stats(df: pd.DataFrame) -> dict[str, Any]:
    """Compute basic statistics from DataFrame with 1-hour cache.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary with statistics
    """
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'memory_usage': df.memory_usage(deep=True).sum(),
        'dtypes': df.dtypes.to_dict(),
        'null_counts': df.isnull().sum().to_dict()
    }


@st.cache_data
def filter_dataframe_cached(df: pd.DataFrame, 
                           column: str, 
                           values: list[Any]) -> pd.DataFrame:
    """Filter DataFrame by column values with caching.
    
    Args:
        df: Input DataFrame
        column: Column name to filter
        values: List of values to keep
        
    Returns:
        Filtered DataFrame
    """
    return df[df[column].isin(values)].copy()


@st.cache_data
def group_and_aggregate_cached(df: pd.DataFrame,
                               group_by: list[str],
                               agg_dict: dict[str, str | list[str]]) -> pd.DataFrame:
    """Group and aggregate DataFrame with caching.
    
    Args:
        df: Input DataFrame
        group_by: Columns to group by
        agg_dict: Aggregation dictionary {column: function}
        
    Returns:
        Aggregated DataFrame
    """
    return df.groupby(group_by).agg(agg_dict).reset_index()


@st.cache_data
def merge_dataframes_cached(df1: pd.DataFrame,
                           df2: pd.DataFrame,
                           on: str | list[str],
                           how: str = 'inner') -> pd.DataFrame:
    """Merge two DataFrames with caching.
    
    Args:
        df1: First DataFrame
        df2: Second DataFrame
        on: Column(s) to merge on
        how: Type of merge ('inner', 'left', 'right', 'outer')
        
    Returns:
        Merged DataFrame
    """
    return pd.merge(df1, df2, on=on, how=how)


@st.cache_data(ttl=600)
def get_unique_values_cached(df: pd.DataFrame, column: str) -> list[Any]:
    """Get unique values from a column with 10-minute cache.
    
    Args:
        df: Input DataFrame
        column: Column name
        
    Returns:
        List of unique values (sorted if possible)
    """
    unique_vals = df[column].dropna().unique().tolist()
    try:
        return sorted(unique_vals)
    except TypeError:
        return unique_vals


def get_file_hash(file_bytes: bytes) -> str:
    """Generate hash for file content to use as cache key.
    
    Args:
        file_bytes: File content as bytes
        
    Returns:
        SHA256 hash string
    """
    return hashlib.sha256(file_bytes).hexdigest()


def clear_all_cache() -> None:
    """Clear all Streamlit cache_data caches."""
    st.cache_data.clear()
    st.success("✅ All caches cleared!")


def clear_specific_cache(cache_func: Callable) -> None:
    """Clear cache for a specific cached function.
    
    Args:
        cache_func: The cached function to clear
    """
    cache_func.clear()
    st.success(f"✅ Cache cleared for {cache_func.__name__}!")
