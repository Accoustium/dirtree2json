/**
* JetBrains Space Automation
* This Kotlin-script file lets you automate build activities
* For more info, see https://www.jetbrains.com/help/space/automation.html
*/

job("Hello World!") {
    startOn {
        gitPush { enabled = true }
        schedule { cron("0 8 * * * *") }
    }

    container("hello-world") {
        resources {
            cpu = 512
            memory = 512
        }
    }
}

job("Hello World!") {
    container("hello-world")
    container("hello-world")
    container("hello-world")
    container("hello-world")
}