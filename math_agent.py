from openai import Agent, Runner, function_tool

# Step 1: Define a simple tool
@function_tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return result"""
    return a + b

@function_tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers and return result"""
    return a * b

# Step 2: Create the Agent
math_agent = Agent(
    name="Math Helper",
    instructions="You are a helpful agent that solves basic math problems.",
    tools=[add_numbers, multiply_numbers],
)

# Step 3: Run the Agent
if __name__ == "__main__":
    result = Runner.run_sync(
        agent=math_agent,
        input="Can you add 15 and 30 for me?",
    )
    print("Agent Response:", result.output_text)
