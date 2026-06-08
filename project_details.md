# 1. Approved Project Title

Medicine Reminder and Health Tracker System

# 2. Problem Statement

Many people forget to take medicines on time and fail to maintain proper health records. This can lead to health complications, missed doses, and poor treatment outcomes. Managing medicine schedules and health information manually can be difficult and time-consuming. Therefore, a Medicine Reminder and Health Tracker System is needed to help users manage medications, receive timely reminders, and maintain health records efficiently.

# 3. Project Objectives

* To provide timely reminders for taking medicines.
* To store and manage medicine schedules.
* To maintain health records such as weight, blood pressure, and sugar levels.
* To reduce missed medication doses.
* To improve personal health monitoring.
* To generate reports for health tracking.

# 4. Module List

## Module 1: User Registration and Login

Allows users to create accounts and securely log in to the system.

## Module 2: Medicine Management

Enables users to add, update, delete, and view medicine details and schedules.

## Module 3: Reminder Management

Generates notifications and reminders based on the medicine schedule.

## Module 4: Health Tracking

Stores and monitors health parameters such as weight, blood pressure, and sugar levels.

## Module 5: Report Generation

Generates reports and summaries of medicine history and health records.

## Module 6: Notification System

Provides alerts and notifications for upcoming medicine schedules.

## Module 7: Admin Dashboard

Allows the administrator to monitor users, medicine records, and system activities.

# 5. Use Case Diagram Submission

## Actors

* User
* Admin

## Use Cases

* Register User
* Login User
* Add Medicine Details
* Update Medicine Schedule
* Delete Medicine Records
* Receive Medicine Reminder
* Track Health Information
* View Health Reports
* Manage User Records
* Monitor System Activities

# 6. Table List

## User Table

* User_ID
* Username
* Password
* Mobile_Number
* Email

## Medicine Table

* Medicine_ID
* User_ID
* Medicine_Name
* Dosage
* Reminder_Time
* Start_Date
* End_Date

## Health Record Table

* Record_ID
* User_ID
* Weight
* Blood_Pressure
* Sugar_Level
* Record_Date

## Reminder Table

* Reminder_ID
* Medicine_ID
* Reminder_Time
* Reminder_Status

## Report Table

* Report_ID
* User_ID
* Report_Type
* Generated_Date

## Admin Table

* Admin_ID
* Username
* Password
