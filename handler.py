import runpod

def handler(job):
    """
    This is a simple handler that takes a name as input and returns a greeting.
    The job parameter contains the input data in job["input"]
    """
    job_input = job["input"]
    
    # Get the name from the input, default to "World" if not provided
    name = job_input.get("name", "World")
    
    
    # Return a greeting message
    return f"Hello, {name}! Welcome to RunPod Serverless! How are you doing?" 
    ####

# Start the serverless function
runpod.serverless.start({"handler": handler})
