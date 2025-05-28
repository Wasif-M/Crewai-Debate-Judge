from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Debate():
	"""Debate crew"""

	agents_config = 'config/agents.yaml'
	task_config="config/tasks.yaml"

	@agent
	def debater_agent(self) -> Agent:
		return Agent(config=self.agents_config['debater_agent'],verbose=True)

	@agent
	def judge_agent(self) -> Agent:
		return Agent(config=self.agents_config['judge_agent'],verbose=True)
	@task
	def propose_task(self) -> Task:
		return Task(config=self.tasks_config['propose_task'],)
	@task
	def oppose_task(self) -> Task:
		return Task(config=self.tasks_config['oppose_task'],)

	@task
	def decide_task(self) -> Task:
		return Task(config=self.tasks_config['decide_task'],)


	@crew
	def crew(self) -> Crew:
		"""Creates the Debate crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)
