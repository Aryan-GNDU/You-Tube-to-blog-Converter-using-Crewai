from crewai import Agent

from tools import yt_tool
from crewai import LLM


llm = LLM(
    model="ollama/granite3-dense:latest",
    base_url="http://localhost:11434"
)
print(llm)

# create a senior blog content reseacher
researcher = Agent(
    role ='blog researcher from YouTube videos',
    goal='get relevant video content for the topic{topic} from YouTube channel',
    verbose=True,
    memory =  True,
    backstory =(
        " expert in understanding videos  in AI Data Science , ML and  Gen AI and providing suggestions for blog content"
    ),tool = [yt_tool],
    llm=llm,
    allow_delegation = True

)


## creating a senior blog writer agent with yt agents

writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False

) 
