import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion,OpenAITextPromptExecutionSettings,AzureTextCompletion
from semantic_kernel.prompt_template import PromptTemplateConfig
from semantic_kernel.contents.chat_history import ChatHistory


service_id:str = "test"

chat_completion = AzureChatCompletion(service_id=service_id, env_file_path=".env")

kernel:Kernel = Kernel()

history = ChatHistory()


kernel.add_service(
    chat_completion
)

aoai_chat_service = AzureChatCompletion(
    service_id="aoai_chat",
)
aoai_text_service = AzureTextCompletion(
    service_id="aoai_text",
)

req_settings = kernel.get_prompt_execution_settings_from_service_id(service_id)
req_settings.max_tokens = 2000
req_settings.temperature = 0.7
req_settings.top_p = 0.8


oai_prompt_execution_settings = OpenAITextPromptExecutionSettings(
    service_id=service_id,
    max_tokens=150,
    temperature=0.7,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    
)

# prompt = """
# 1) A robot may not injure a human being or, through inaction,
# allow a human being to come to harm.

# 2) A robot must obey orders given it by human beings except where
# such orders would conflict with the First Law.

# 3) A robot must protect its own existence as long as such protection
# does not conflict with the First or Second Law.

# Give me the TLDR in exactly 5 words."""

prompt = input("Please enter a prompt\n")


prompt_template_config = PromptTemplateConfig(
    template=prompt,
    name="tldr",
    template_format="semantic-kernel",
    execution_settings=req_settings,
)

function = kernel.add_function(
    function_name="tldr_function",
    plugin_name="tldr_plugin",
    prompt_template_config=prompt_template_config,
)

stream =  aoai_chat_service.get_streaming_chat_message_contents(prompt=prompt,settings=oai_prompt_execution_settings,chat_history=history)

async def main():
    # result  = await kernel.invoke(function)
    # print(result)
    async for message in stream:
        print(str(message[0]), end="")


if __name__ == '__main__':
    asyncio.run(main())