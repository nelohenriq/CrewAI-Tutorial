from dotenv import load_dotenv
from crewai import Crew
from tasks import MeetingPrepTasks
from agents import MettingPrepAgents
from tools import ExaSearchToolSet


def main():
    load_dotenv()


if __name__ == "__main__":
    main()
