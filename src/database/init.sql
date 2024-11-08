
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

CREATE TABLE degrees (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	created_at TIMESTAMP DEFAULT now() NOT NULL, 
	CONSTRAINT degrees_pkey PRIMARY KEY (id)
)

;
INSERT INTO degrees VALUES ('bd65a7e0-b4ac-4e2b-ac89-03e360f32357', 'Alfredo', False, 2024-10-27 21:47:20.172478);
INSERT INTO degrees VALUES ('3f432802-d7a7-46b3-ba42-1cd0b9d7503e', 'test', True, 2024-10-27 21:51:19.282643);
INSERT INTO degrees VALUES ('65797850-6692-48d7-9927-65e42d5cfc37', 'test', True, 2024-10-27 21:51:24.451474);
INSERT INTO degrees VALUES ('a2489afd-30e0-416a-afe8-2b001784df4f', 'test', False, 2024-10-27 21:50:52.226924);
INSERT INTO degrees VALUES ('0fe0448d-73f0-48c5-9167-bfb82cd9724d', 'test', False, 2024-10-27 21:51:25.640963);
INSERT INTO degrees VALUES ('c78b1c6d-6bfa-46e4-870c-208549170d63', 'millonarios', True, 2024-10-27 21:50:34.291118);

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
INSERT INTO users VALUES ('teacher-user-id', '02', 'Teacher User', 'teacher@example.com', '1234567891', True, 2024-10-29 03:09:23.233425);
INSERT INTO users VALUES ('student-user-id', '03', 'Student User', 'student@example.com', '1234567892', True, 2024-10-29 03:09:23.383171);

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
INSERT INTO login VALUES ('teacher-login-id', 'teacher-user-id', 'teacher', '1234', True, 2024-10-29 03:09:23.310846);
INSERT INTO login VALUES ('student-login-id', 'student-user-id', 'student', '1234', True, 2024-10-29 03:09:23.474414);

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
INSERT INTO students VALUES ('student-test-id', 'student-user-id', 'bd65a7e0-b4ac-4e2b-ac89-03e360f32357', 3.5, True, 2024-10-29 03:10:49.502519);

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
