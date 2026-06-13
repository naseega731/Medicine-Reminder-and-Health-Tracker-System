# Database Schema Creation

## Project Title

Medicine Reminder and Health Tracker System

## Database Used

SQLite

---

## Table 1: User

| Field Name    | Data Type | Description    |
| ------------- | --------- | -------------- |
| User_ID       | INTEGER   | Primary Key    |
| Username      | TEXT      | User Name      |
| Password      | TEXT      | User Password  |
| Email         | TEXT      | User Email     |
| Mobile_Number | TEXT      | Contact Number |

Primary Key: User_ID

---

## Table 2: Medicine

| Field Name    | Data Type | Description        |
| ------------- | --------- | ------------------ |
| Medicine_ID   | INTEGER   | Primary Key        |
| User_ID       | INTEGER   | Foreign Key        |
| Medicine_Name | TEXT      | Medicine Name      |
| Dosage        | TEXT      | Dosage Information |
| Reminder_Time | TEXT      | Reminder Time      |
| Start_Date    | TEXT      | Start Date         |
| End_Date      | TEXT      | End Date           |

Primary Key: Medicine_ID

Foreign Key: User_ID

---

## Table 3: Health_Record

| Field Name     | Data Type | Description |
| -------------- | --------- | ----------- |
| Record_ID      | INTEGER   | Primary Key |
| User_ID        | INTEGER   | Foreign Key |
| Weight         | REAL      | Weight      |
| Blood_Pressure | TEXT      | BP Value    |
| Blood_Sugar    | REAL      | Sugar Level |
| Heart_Rate     | INTEGER   | Heart Rate  |
| Record_Date    | TEXT      | Date        |

Primary Key: Record_ID

Foreign Key: User_ID

---

## Table 4: Reminder

| Field Name    | Data Type | Description       |
| ------------- | --------- | ----------------- |
| Reminder_ID   | INTEGER   | Primary Key       |
| Medicine_ID   | INTEGER   | Foreign Key       |
| Reminder_Time | TEXT      | Reminder Time     |
| Status        | TEXT      | Pending/Completed |

Primary Key: Reminder_ID

Foreign Key: Medicine_ID

---

## Entity Relationships

User (1) ------ (M) Medicine

User (1) ------ (M) Health_Record

Medicine (1) ------ (M) Reminder

---

## Database Summary

The database schema is designed using SQLite. It stores user information, medicine schedules, reminder details, and health records. Relationships between tables ensure efficient data management and retrieval.
