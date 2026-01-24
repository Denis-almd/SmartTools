import streamlit as st
from project.tools.base_tool import BaseTool

class TimeConverter(BaseTool):
    def get_name(self) -> str:
        return "Time Converter"
    
    def get_icon(self) -> str:
        return "⏰"
    
    def get_description(self) -> str:
        return "Convert time between HH:MM:SS format and total seconds."

    def render(self):
        st.header("Convert HH:MM:SS to Seconds and Vice Versa ⏰")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("HH:MM:SS → Seconds")
            time_input = st.text_input(
                "Time:", 
                placeholder="01:30:45",
                key="time_to_sec",
                help="Format: HH:MM:SS"
            )
            if time_input:
                self._convert_time_to_seconds(time_input)
    
        with col2:
            st.subheader("Seconds → HH:MM:SS")
            sec_input = st.number_input(
                "Seconds:", 
                min_value=0, 
                step=1,
                key="sec_to_time"
            )
            if sec_input > 0:
                hhmmss = self._convert_seconds_to_hhmmss(sec_input)
                st.success(f"**{sec_input}** seconds = **{hhmmss}**")
        

    def _convert_time_to_seconds(self, time_str: str):
        try:
            parts = time_str.split(':')
            if len(parts) != 3:
                st.warning("⚠️ Use format HH:MM:SS")
                return
            
            h, m, s = map(int, parts)
            
            # Validação de valores
            if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
                st.error("❌ Invalid time! Hours: 0-23, Minutes/Seconds: 0-59")
                return
            
            total = h * 3600 + m * 60 + s
            st.success(f"**{time_str}** = **{total:}** seconds")
        except ValueError:
            st.error("❌ Invalid format. Use only numbers and ':' (HH:MM:SS)")
        
    def _convert_seconds_to_hhmmss(self, total_seconds: int) -> str:
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return f"{h:02}:{m:02}:{s:02}"