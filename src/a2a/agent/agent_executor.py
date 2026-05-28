import logging

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.types import (
    TaskArtifactUpdateEvent,
    TaskState,
    TaskStatus,
    TaskStatusUpdateEvent,
)
from a2a.utils import (
    new_agent_text_message,
    new_task,
    new_text_artifact,
)

# region --- Imports for Agent Framework-based Product Management Agent ---
from .product_management_agent import AgentFrameworkProductManagementAgent

logger = logging.getLogger(__name__)



class AgentFrameworkProductManagementExecutor(AgentExecutor):
    """AgentFrameworkProductManagement Executor for A2A Protocol"""

    # Instantiates a AgentFrameworkProductManagementAgent for use in the class
    def __init__(self):
        self.agent = AgentFrameworkProductManagementAgent()

    # processes the incoming request, retrieves the user input, and uses 
    # the AgentFrameworkProductManagementAgent to handle the request. 
    # It streams partial responses and enqueues events to the event queue 
    # based on the agent’s output. The cancel method is a placeholder 
    # for task cancellation functionality, which is not implemented in this example.
    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        """Execute agent request with A2A protocol support
        
        Args:
            context: Request context containing user input and task info
            event_queue: Event queue for publishing task updates
        """
        query = context.get_user_input()
        task = context.current_task
        if not task:
            task = new_task(context.message)
            await event_queue.enqueue_event(task)

        async for partial in self.agent.stream(query, task.contextId):
            require_input = partial['require_user_input']
            is_done = partial['is_task_complete']
            text_content = partial['content']

            if require_input:
                await event_queue.enqueue_event(
                    TaskStatusUpdateEvent(
                        status=TaskStatus(
                            state=TaskState.input_required,
                            message=new_agent_text_message(
                                text_content,
                                task.contextId,
                                task.id,
                            ),
                        ),
                        final=True,
                        contextId=task.contextId,
                        taskId=task.id,
                    )
                )
            elif is_done:
                await event_queue.enqueue_event(
                    TaskArtifactUpdateEvent(
                        append=False,
                        contextId=task.contextId,
                        taskId=task.id,
                        lastChunk=True,
                        artifact=new_text_artifact(
                            name='current_result',
                            description='Result of request to agent.',
                            text=text_content,
                        ),
                    )
                )
                await event_queue.enqueue_event(
                    TaskStatusUpdateEvent(
                        status=TaskStatus(state=TaskState.completed),
                        final=True,
                        contextId=task.contextId,
                        taskId=task.id,
                    )
                )
            else:
                await event_queue.enqueue_event(
                    TaskStatusUpdateEvent(
                        status=TaskStatus(
                            state=TaskState.working,
                            message=new_agent_text_message(
                                text_content,
                                task.contextId,
                                task.id,
                            ),
                        ),
                        final=False,
                        contextId=task.contextId,
                        taskId=task.id,
                    )
                )

    async def cancel(
        self, context: RequestContext, event_queue: EventQueue
    ) -> None:
        """Cancel the current task execution"""
        logger.warning("Task cancellation requested but not implemented")
        raise Exception('cancel not supported')


