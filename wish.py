import streamlit as st
import time
import numpy as np

progress_bar = st.progress(0)
status_text = st.empty()

for i in range(25):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = list(range(25))

    # Update status text.
    status_text.text(
        'Day %s of January' % new_rows[i])

    # Append data to the chart.
    # Pretend we're doing some computation that takes time.
    time.sleep(0.5)

status_text.text('Happy Birthday!')
st.balloons()