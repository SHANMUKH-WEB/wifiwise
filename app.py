
import streamlit as st

st.set_page_config(
    page_title="WiFiWise AI",
    page_icon="📶",
    layout="wide"
)

st.title("📶 WiFiWise AI")
st.caption("Your personal Wi-Fi intelligence assistant")

st.markdown(
    "Understand connection problems and assess Wi-Fi "
    "for your travel, work, and study needs."
)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("🎯 TaskFit AI")

    task = st.selectbox(
        "What do you want to do?",
        [
            "Video meeting",
            "Online class",
            "Upload a file",
            "Online gaming",
            "Browse websites"
        ]
    )

    speed = st.number_input(
        "Download speed (Mbps)",
        min_value=0.0,
        value=10.0
    )

    latency = st.number_input(
        "Latency (milliseconds)",
        min_value=0.0,
        value=50.0
    )

    if st.button("Assess Connection"):
        st.write("Selected task:", task)

        if latency > 100:
            st.warning(
                "High latency may affect interactive activities."
            )
        elif speed < 5:
            st.warning(
                "Low download speed may affect some activities."
            )
        else:
            st.success(
                "Your entered measurements look promising. "
                "Actual performance may vary."
            )

with right:
    st.subheader("🕵️ AI Troubleshooter")

    problem = st.selectbox(
        "Choose your problem",
        [
            "Slow internet",
            "Connected but no internet",
            "Frequent disconnections",
            "Login page not appearing",
            "High latency"
        ]
    )

    details = st.text_area(
        "Describe what happened",
        placeholder="Example: Hotel Wi-Fi disconnects during calls."
    )

    if st.button("Get Troubleshooting Tips"):
        st.write("Problem:", problem)

        st.info(
            "Check the guest login page, reconnect to the "
            "network, and test another website. If the issue "
            "continues, ask the hotel or café staff for help."
        )

st.divider()

st.subheader("📊 Connection Measurements")
st.write(
    "Live connection testing will be added in the next stage."
)

st.subheader("📝 Smart Reception Report")

if st.button("Generate Reception Message"):
    st.text_area(
        "Message to staff",
        value=(
            f"Hello, I am experiencing '{problem}' while "
            f"using the guest Wi-Fi. Could you please check "
            f"whether the network is working correctly?"
        ),
        key="reception_message"
    )
