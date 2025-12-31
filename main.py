import sys
import os

# Add project root to path ensuring submodules can resolve each other
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from finance_assistance_agent.agent import root_agent
    print("Successfully imported root_agent.")
except ImportError as e:
    print(f"Error importing root_agent: {e}")
    sys.exit(1)

if __name__ == "__main__":
    print(f"Starting {root_agent.name}...")
    if hasattr(root_agent, 'run'):
        print("Found run method, executing...")
        root_agent.run()
    else:
        print("Agent loaded successfully. No 'run' method found.")
