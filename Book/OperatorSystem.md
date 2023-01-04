# Multitasking in mobile systems
## IOS:
- The iOS4 programming API provides support for multitasking, thus allowing a process to run in the background without beign suspended. Howerver, it is limited and only available for a limited number of applications types, including applications:
-	Running a single, finite-length task (such as completing a download of content from a network).
-	Receiving notifications of an event occurring.
-	With long-running background tasks.
## Android
- Applications can run in the background. If an application requires processing while in the background, the application must use a **service**, a separate application component that runs on behalf of the background process. Consider a streaming audio application: if the application moves to the background, the service continues to send audio files to the audio device driver on behalf of the background application
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjU3NjgyODQ5LC0yMDg4NzQ2NjEyLC0xMz
gxMTgwODk1LDczMDk5ODExNl19
-->