
CREATE TABLE classrooms (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	type VARCHAR(50) NOT NULL, 
	capacity INTEGER NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT classrooms_pkey PRIMARY KEY (id)
)

;
INSERT INTO classrooms VALUES ('classroom-1', 'Room A', 'Lecture', 30, True, 2024-10-29 03:36:24.643133);
INSERT INTO classrooms VALUES ('classroom-2', 'Room B', 'Lab', 20, True, 2024-10-29 03:36:24.769150);
INSERT INTO classrooms VALUES ('classroom-3', 'Room C', 'Seminar', 15, True, 2024-10-29 03:36:24.831174);

CREATE TABLE degrees (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT degrees_pkey PRIMARY KEY (id)
)

;
INSERT INTO degrees VALUES ('bd65a7e0-b4ac-4e2b-ac89-03e360f32357', 'Alfredo', False, 2024-10-27 21:47:20.172478);
INSERT INTO degrees VALUES ('a2489afd-30e0-416a-afe8-2b001784df4f', 'test', False, 2024-10-27 21:50:52.226924);
INSERT INTO degrees VALUES ('0fe0448d-73f0-48c5-9167-bfb82cd9724d', 'test', False, 2024-10-27 21:51:25.640963);
INSERT INTO degrees VALUES ('3f432802-d7a7-46b3-ba42-1cd0b9d7503e', 'test', False, 2024-10-27 21:51:19.282643);
INSERT INTO degrees VALUES ('c78b1c6d-6bfa-46e4-870c-208549170d63', 'millonarios', False, 2024-10-27 21:50:34.291118);
INSERT INTO degrees VALUES ('65797850-6692-48d7-9927-65e42d5cfc37', 'test', False, 2024-10-27 21:51:24.451474);
INSERT INTO degrees VALUES ('6fcc4bb9-e45e-40d8-8ab3-4e84e6469eb5', 'Millox', False, 2024-10-29 09:23:10.083478);
INSERT INTO degrees VALUES ('479a5220-7422-48ab-9bde-10d15de05572', 'Once A1', False, 2024-10-29 09:57:26.144818);
INSERT INTO degrees VALUES ('4f464461-74f8-4010-80e8-d022a9b6755d', 'Once 2', False, 2024-10-29 08:28:08.973214);
INSERT INTO degrees VALUES ('1ba86267-be95-4973-b613-c8b650b1da06', 'Millitos', True, 2024-10-29 09:59:01.491801);
INSERT INTO degrees VALUES ('8753472e-7d6b-4942-9c2a-448fda8f633f', 'Upload', False, 2024-10-29 10:15:17.692993);

CREATE TABLE roles (
	id VARCHAR NOT NULL, 
	rol VARCHAR NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT roles_pkey PRIMARY KEY (id)
)

;
INSERT INTO roles VALUES ('01', 'admin', True, 2024-10-29 03:07:32.330014);
INSERT INTO roles VALUES ('02', 'teacher', True, 2024-10-29 03:07:32.387182);
INSERT INTO roles VALUES ('03', 'student', True, 2024-10-29 03:07:32.444716);

CREATE TABLE subjects (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT subjects_pkey PRIMARY KEY (id)
)

;
INSERT INTO subjects VALUES ('subject-1', 'Mathematics', True, 2024-10-29 03:36:24.887682);
INSERT INTO subjects VALUES ('subject-2', 'Physics', True, 2024-10-29 03:36:24.977553);
INSERT INTO subjects VALUES ('subject-3', 'Chemistry', True, 2024-10-29 03:36:25.032613);
INSERT INTO subjects VALUES ('subject-4', 'Biology', True, 2024-10-29 03:36:25.121542);

CREATE TABLE users (
	id VARCHAR NOT NULL, 
	role_id VARCHAR NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
	phone_number VARCHAR(15) NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT users_pkey PRIMARY KEY (id), 
	CONSTRAINT users_role_id_fkey FOREIGN KEY(role_id) REFERENCES roles (id) ON DELETE CASCADE
)

;
INSERT INTO users VALUES ('admin-user-id', '01', 'Admin User', 'admin@example.com', '1234567890', True, 2024-10-29 03:09:23.094453);
INSERT INTO users VALUES ('2d9f2718-9209-49c1-bd7b-641c05e9b73d', '02', 'Los bosteros', 'son@asi.com', '312312', True, 2024-10-30 11:04:11.143144);
INSERT INTO users VALUES ('teacher-user-id', '02', 'aaaaa', '12312@gmail.com', '1234567891', True, 2024-10-29 03:09:23.233425);
INSERT INTO users VALUES ('9b7d7691-2e1f-4401-9ef3-2c7ef512cb41', '02', 'Yuliana', '', '3123123', True, 2024-10-30 11:19:42.114507);
INSERT INTO users VALUES ('3b3a7e2f-c816-443b-b8d2-135497b80576', '02', 'MIguel', 'quiles@quiles.com', '312', True, 2024-10-30 11:31:38.295062);
INSERT INTO users VALUES ('b6c96410-bb2a-4efa-83bb-5b7af9e450c2', '02', 'Porque se fue?', 'porque@murio.com', '123123', True, 2024-10-30 11:45:30.850107);
INSERT INTO users VALUES ('student-user-id', '03', 'admin', 'student@example.com', '1234567892', True, 2024-10-29 03:09:23.383171);
INSERT INTO users VALUES ('6d1b21b3-d48b-4d24-a4ca-d864557c477d', '02', 'Here we go', 'aa2@asd.com', '123', True, 2024-10-30 22:22:59.236280);

CREATE TABLE admins (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT admins_pkey PRIMARY KEY (id), 
	CONSTRAINT admins_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
)

;

CREATE TABLE login (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(100) NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT login_pkey PRIMARY KEY (id), 
	CONSTRAINT login_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
)

;
INSERT INTO login VALUES ('admin-login-id', 'admin-user-id', 'admin', '1234', True, 2024-10-29 03:09:23.170899);
INSERT INTO login VALUES ('student-login-id', 'student-user-id', 'student', '1234', True, 2024-10-29 03:09:23.474414);
INSERT INTO login VALUES ('a870f6b6-5b21-4287-929c-b5130bb931df', '2d9f2718-9209-49c1-bd7b-641c05e9b73d', 'los.son', 'gwkdQnwlWF', True, 2024-10-30 11:04:11.143144);
INSERT INTO login VALUES ('teacher-login-id', 'teacher-user-id', 'admin', '1234232323', True, 2024-10-29 03:09:23.310846);
INSERT INTO login VALUES ('1ed3a695-07e4-4c01-89c1-3f4897bc15ec', '9b7d7691-2e1f-4401-9ef3-2c7ef512cb41', 'admin', '1234', True, 2024-10-30 11:19:42.114507);
INSERT INTO login VALUES ('3f805adb-35c6-445b-b8d9-e451bdc3882c', '3b3a7e2f-c816-443b-b8d2-135497b80576', 'Quiles', '1234', True, 2024-10-30 11:31:38.295062);
INSERT INTO login VALUES ('9936577c-e3e3-441c-93a6-b2a152082c95', 'b6c96410-bb2a-4efa-83bb-5b7af9e450c2', 'porque.porque', 'Ji3psZYsYE', True, 2024-10-30 11:45:30.850107);
INSERT INTO login VALUES ('2d9c3afe-d2e3-4423-9c0a-b0f63738970b', '6d1b21b3-d48b-4d24-a4ca-d864557c477d', 'aaaa.aa2', '1234', True, 2024-10-30 22:22:59.236280);

CREATE TABLE students (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	degree_id VARCHAR NOT NULL, 
	gpa DOUBLE PRECISION NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT students_pkey PRIMARY KEY (id), 
	CONSTRAINT students_degree_id_fkey FOREIGN KEY(degree_id) REFERENCES degrees (id) ON DELETE CASCADE, 
	CONSTRAINT students_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
)

;
INSERT INTO students VALUES ('c2b4ee68-4f76-4c52-9e77-0a81fd16abdb', 'b6c96410-bb2a-4efa-83bb-5b7af9e450c2', '0fe0448d-73f0-48c5-9167-bfb82cd9724d', 23.0, False, 2024-10-30 11:45:30.850107);
INSERT INTO students VALUES ('student-test-id', 'student-user-id', 'bd65a7e0-b4ac-4e2b-ac89-03e360f32357', 0.0, False, 2024-10-29 03:10:49.502519);
INSERT INTO students VALUES ('1add0543-3565-49ff-a65a-23c5974ff3f9', '6d1b21b3-d48b-4d24-a4ca-d864557c477d', '1ba86267-be95-4973-b613-c8b650b1da06', 0.0, True, 2024-10-30 22:22:59.236280);

CREATE TABLE teachers (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	salary DOUBLE PRECISION NOT NULL, 
	specialization VARCHAR(100) NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT teachers_pkey PRIMARY KEY (id), 
	CONSTRAINT teachers_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
)

;
INSERT INTO teachers VALUES ('teacher-2', 'teacher-user-id', 123.0, '123', False, 2024-10-29 03:36:25.322261);
INSERT INTO teachers VALUES ('teacher-3', 'teacher-user-id', 60000.0, 'Chemistry', False, 2024-10-29 03:36:25.410720);
INSERT INTO teachers VALUES ('b7a140e0-3a89-4c89-926b-20aee07408e9', '2d9f2718-9209-49c1-bd7b-641c05e9b73d', 1232323.0, 'amargos', False, 2024-10-30 11:04:11.143144);
INSERT INTO teachers VALUES ('teacher-1', 'teacher-user-id', 0.0, '', False, 2024-10-29 03:36:25.215034);
INSERT INTO teachers VALUES ('cdaf572f-c459-4aba-8d88-f0526c4d3c81', '9b7d7691-2e1f-4401-9ef3-2c7ef512cb41', 0.0, 'asdsdasdasda', True, 2024-10-30 11:19:42.114507);
INSERT INTO teachers VALUES ('2096f9ec-e88c-4ac0-a600-280474a6a85f', '3b3a7e2f-c816-443b-b8d2-135497b80576', 0.0, 'asdsdasdasda', True, 2024-10-30 11:31:38.295062);

CREATE TABLE courses (
	id VARCHAR NOT NULL, 
	classroom_id VARCHAR NOT NULL, 
	subject_id VARCHAR NOT NULL, 
	degrees_id VARCHAR NOT NULL, 
	teacher_id VARCHAR NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT courses_pkey PRIMARY KEY (id), 
	CONSTRAINT courses_classroom_id_fkey FOREIGN KEY(classroom_id) REFERENCES classrooms (id) ON DELETE CASCADE, 
	CONSTRAINT courses_degrees_id_fkey FOREIGN KEY(degrees_id) REFERENCES degrees (id) ON DELETE CASCADE, 
	CONSTRAINT courses_subject_id_fkey FOREIGN KEY(subject_id) REFERENCES subjects (id) ON DELETE CASCADE, 
	CONSTRAINT courses_teacher_id_fkey FOREIGN KEY(teacher_id) REFERENCES teachers (id) ON DELETE CASCADE
)

;
INSERT INTO courses VALUES ('course-1', 'classroom-1', 'subject-1', '3f432802-d7a7-46b3-ba42-1cd0b9d7503e', 'teacher-1', True, 2024-10-29 03:36:25.515107);
INSERT INTO courses VALUES ('course-2', 'classroom-2', 'subject-2', '65797850-6692-48d7-9927-65e42d5cfc37', 'teacher-2', True, 2024-10-29 03:36:25.697200);
INSERT INTO courses VALUES ('course-3', 'classroom-3', 'subject-3', 'c78b1c6d-6bfa-46e4-870c-208549170d63', 'teacher-3', True, 2024-10-29 03:36:25.776864);

CREATE TABLE schedules (
	id VARCHAR NOT NULL, 
	course_id VARCHAR NOT NULL, 
	start_time VARCHAR(30) NOT NULL, 
	end_time VARCHAR(30) NOT NULL, 
	day_of_week VARCHAR(30) NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT schedules_pkey PRIMARY KEY (id), 
	CONSTRAINT schedules_course_id_fkey FOREIGN KEY(course_id) REFERENCES courses (id) ON DELETE CASCADE
)

;
INSERT INTO schedules VALUES ('schedule-1', 'course-1', '09:00 AM', '10:30 AM', 'Monday', True, 2024-10-29 03:36:25.840175);
INSERT INTO schedules VALUES ('schedule-2', 'course-2', '11:00 AM', '12:30 PM', 'Tuesday', True, 2024-10-29 03:36:25.905796);
INSERT INTO schedules VALUES ('schedule-3', 'course-3', '01:00 PM', '02:30 PM', 'Wednesday', True, 2024-10-29 03:36:25.958899);
