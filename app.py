import streamlit as st

st.set_page_config(
	page_title="CyberBot",
	page_icon="🔐"
)

st.title("🔐 CyberBot")
st.subheader("Your Cybersecurity Assistant")

st.write(
	"Hello! I am CyberBot. "
	"Ask me a basic cybersecurity question."
)

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.write(message["content"])

question = st.chat_input("Ask me something...")

if question:
	st.session_state.messages.append({
		"role": "user",
		"content": question
	})

	text = question.lower()

	if "phishing" in text:
		answer = (
			"Phishing is a scam where attackers try "
			"to steal your information using fake "
			"messages, emails, or websites."
		)
	elif "password" in text:
		answer = (
			"Use a long, unique password for each "
			"account. A password manager can help."
		)
	elif "malware" in text:
		answer = (
			"Malware is harmful software designed "
			"to damage devices or steal information."
		)
	elif "cybersecurity" in text:
		answer = (
			"Cybersecurity protects computers, "
			"networks, and data from digital attacks."
		)
	elif "hello" in text or "hi" in text:
		answer = "Hello! 👋 How can I help you stay safe online?"
	else:
		answer = (
			"I don't know that answer yet. Try asking "
			"about phishing, passwords, malware, or cybersecurity."
		)

	st.session_state.messages.append({
		"role": "assistant",
		"content": answer
	})

	st.rerun()
