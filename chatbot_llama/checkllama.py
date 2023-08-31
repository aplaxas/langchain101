import requests
import os
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from huggingface_hub import InferenceClient

# https://python.langchain.com/docs/integrations/llms/huggingface_hub

HUGGINGFACEHUB_API_TOKEN = "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"

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# print(HUGGINGFACEHUB_API_TOKEN)


text = """DPS# 748700319 SR# 170809767 CALL# 00T6P00000KQKT3UAI
SFDC# 170809767
Web Inbound
Id:Primary;First Name:Nesa;
Last Name:Kandaiah;
Email:nesa316@gmail.com;
Phone:8045024453;
PreferredContactLanguage:English;
PreferredModeOfContact:Email; Id:Parts Dispatch Address;
 First Name:Nesa;
 Last Name:Kandaiah;
 Phone:8045024453; AddressLine1:11 Westcott Pkwy; City:St Augustine;
 State Province:FD;
 Country:UY;
 Zip Postal Code:32095;
DISPATCH_NOTES:	NA;
Resolution Info:	customer is experiencing Microsoft windows os issues;
Alert value description:	MICROSOFTWINDOWSOS : Hi there have been persistent issues impacting the overall user experience.
The most prevalent problem is with the computers hibernation feature. It consistently struggles to wake from hibernation, often requiring multiple hard reset . This is not only disruptive but also hampers productivity significantly.
Additionally, I have been experiencing system instability, particularly when the PC is left idle for certain periods. The machine frequently displays a blue screen error, causing unscheduled interruptions and potential data loss.
In an effort to rectify these issues, I have already performed a full system reset and reinstalled the Windows operating system. Regrettably, these steps have not resolved the problems; they persist in the same manner.
I kindly request your technical support team to provide further troubleshooting assistance or arrange a service appointment if deemed necessary.;
Severity:	MAJOR;
EventID:	;
TrapOID:	MICROSOFTWINDOWSOS;
PartSerialNo:	;
EventObject:	Unknown event object;
Device name:	ALIEN-R15;
Device IP address:	192.168.29.240;
Device OS:	Microsoft Windows 11 Home;
Client host name:	ALIEN-R15;
Client IP address:	192.168.29.240;
Diagnostics opt in:	NO;
Preferred Contact Method:	email;
Preferred Contact Time:	ANYTIME;
Time Zone :	GMT;
Alternate Email Address:	N/A;
Linked TechDirect Account:	N/A;"""

template = """summarize problem or issues from the following text 
{text}"""

prompt = PromptTemplate(template=template, input_variables=["text"])

repo_id = "meta-llama/Llama-2-7b-chat-hf"

llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(text))


# question = "Who won the FIFA World Cup in the year 1994? "
# template = """Question: {question}
# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# repo_id = "meta-llama/Llama-2-7b-chat-hf"

# llm = HuggingFaceHub(
#     repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
# )
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# print(llm_chain.run(question))
