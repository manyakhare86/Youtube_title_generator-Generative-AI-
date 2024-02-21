from openai import OpenAI
import time
import streamlit as st

client = OpenAI(api_key="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")


assistant_id = "asst_IVma5pi2W4r9RXh3TTOXovO1"

def create_thread(ass_id,prompt):
    #Get Assitant
    assistant = client.beta.assistants.retrieve("asst_IVma5pi2W4r9RXh3TTOXovO1")

    #create a thread
    thread = client.beta.threads.create()
    my_thread_id = thread.id


    #create a message
    message = client.beta.threads.messages.create(
        thread_id=my_thread_id,
        role="user",
        content=prompt
    )

    #run
    run = client.beta.threads.runs.create(
        thread_id=my_thread_id,
        assistant_id=ass_id,
    ) 

    return run.id, thread.id


def check_status(run_id,thread_id):
    run = client.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id,
    )
    return run.status

st.title("Yoututbe Video Title Generator")
st.subheader("Get best headings for your video")
prompt = st.text_input("Enter your topic here:")

if st.button("Generate Title"):
    with st.spinner("Generating best titles"):
        my_run_id, my_thread_id = create_thread(assistant_id,f"[topic]: {prompt}")

        status = check_status(my_run_id,my_thread_id)

        while (status != "completed"):
            status = check_status(my_run_id,my_thread_id)
            time.sleep(2)


        response = client.beta.threads.messages.list(
        thread_id=my_thread_id
        )
        

        if response.data:
            st.text_area("List of Titles",response.data[0].content[0].text.value, height=300)
            st.success("Done!")
            # print(response.data[0].content[0].text.value)