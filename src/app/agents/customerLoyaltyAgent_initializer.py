# An “agent initializer” is not a class, and it does not invoke the agent at chat time.
# It is a setup script that creates/registers an agent definition in Azure AI Foundry.
# reads the cart manager prompt from prompts/CartManagerPrompt.txt
# creates an AIProjectClient
# loads the tools
# calls initialize_agent(...)
# A better name would be something like agent registration script or agent deployment script.

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
from tool_definitions import get_tools_for_agent_oneshot
from agent_initializer import initialize_agent
import asyncio

load_dotenv()

# Read the prompt template for the customer loyalty agent from a text file. This prompt provides the agent with instructions 
# on how to assist customers with loyalty-related inquiries, such as calculating discounts based on their loyalty tier and 
# transaction history. The prompt is stored in the prompts directory at the root of the project.
CL_PROMPT_TARGET = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'prompts', 'CustomerLoyaltyAgentPrompt.txt')
with open(CL_PROMPT_TARGET, 'r', encoding='utf-8') as file:
    CL_PROMPT = file.read()

project_endpoint = os.environ["FOUNDRY_ENDPOINT"]

project_client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),
)

# Define the set of user-defined callable functions to use as tools (from MCP client)
# References a function called get_tools_for_agent_oneshot() in src/app/agents/tool_definitions.py. 
# This async function discovers the available tools from the MCP server, closes the MCP connection cleanly, 
# and returns the FunctionTool objects that the specified agent type needs. In this case, it returns the 
# mcp_calculate_discount tool for the customer loyalty agent. When invoked by the agent, mcp_calculate_discount() 
# calls get_customer_discount() on the MCP server, which in turn calls calculate_discount() in src/app/tools/discountLogic.py.
# This function takes a customer ID and returns a discount percentage based on the customer's loyalty tier. 
# You can review the code in this file to understand how it works. 
# This particular tool is more complex than others because it communicates with the GPT model to determine the appropriate discount based on the customer's transaction history. It also simulates connecting to two separate databases to retrieve customer information.
functions = asyncio.run(get_tools_for_agent_oneshot("customer_loyalty"))

# This code initializes the agent with the specified model, name, instructions, and toolset. It then creates the agent in Microsoft Foundry
# and prints the agent ID to the console. We have prepopulated your .env file with the appropriate agent names, so be sure not to change this name.
initialize_agent(
    project_client=project_client,
    model=os.environ["gpt_deployment"],
    name="customer-loyalty",
    description="Zava Customer Loyalty Agent",
    instructions=CL_PROMPT,
    tools=functions
)