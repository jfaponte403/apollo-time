
CREATE TABLE classrooms (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	type VARCHAR(50) NOT NULL, 
	capacity INTEGER NOT NULL, 
	CONSTRAINT classrooms_pkey PRIMARY KEY (id)
)

;

CREATE TABLE degrees (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	CONSTRAINT degrees_pkey PRIMARY KEY (id)
)

;

CREATE TABLE roles (
	id VARCHAR NOT NULL, 
	rol VARCHAR NOT NULL, 
	CONSTRAINT roles_pkey PRIMARY KEY (id)
)

;

CREATE TABLE subjects (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	CONSTRAINT subjects_pkey PRIMARY KEY (id)
)

;

CREATE TABLE users (
	id VARCHAR NOT NULL, 
	role_id VARCHAR NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
	phone_number VARCHAR(15) NOT NULL, 
	CONSTRAINT users_pkey PRIMARY KEY (id), 
	CONSTRAINT users_role_id_fkey FOREIGN KEY(role_id) REFERENCES roles (id)
)

;

CREATE TABLE admins (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	CONSTRAINT admins_pkey PRIMARY KEY (id), 
	CONSTRAINT admins_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id)
)

;

CREATE TABLE login (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(100) NOT NULL, 
	CONSTRAINT login_pkey PRIMARY KEY (id), 
	CONSTRAINT login_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id)
)

;

CREATE TABLE students (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	degree_id VARCHAR NOT NULL, 
	gpa DOUBLE PRECISION NOT NULL, 
	CONSTRAINT students_pkey PRIMARY KEY (id), 
	CONSTRAINT students_degree_id_fkey FOREIGN KEY(degree_id) REFERENCES degrees (id), 
	CONSTRAINT students_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id)
)

;

CREATE TABLE teachers (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	salary DOUBLE PRECISION NOT NULL, 
	specialization VARCHAR(100) NOT NULL, 
	CONSTRAINT teachers_pkey PRIMARY KEY (id), 
	CONSTRAINT teachers_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id)
)

;

CREATE TABLE courses (
	id VARCHAR NOT NULL, 
	classroom_id VARCHAR NOT NULL, 
	subject_id VARCHAR NOT NULL, 
	degrees_id VARCHAR NOT NULL, 
	teacher_id VARCHAR NOT NULL, 
	CONSTRAINT courses_pkey PRIMARY KEY (id), 
	CONSTRAINT courses_classroom_id_fkey FOREIGN KEY(classroom_id) REFERENCES classrooms (id), 
	CONSTRAINT courses_degrees_id_fkey FOREIGN KEY(degrees_id) REFERENCES degrees (id), 
	CONSTRAINT courses_subject_id_fkey FOREIGN KEY(subject_id) REFERENCES subjects (id), 
	CONSTRAINT courses_teacher_id_fkey FOREIGN KEY(teacher_id) REFERENCES teachers (id)
)

;

CREATE TABLE schedules (
	id VARCHAR NOT NULL, 
	course_id VARCHAR NOT NULL, 
	start_time VARCHAR(30) NOT NULL, 
	end_time VARCHAR(30) NOT NULL, 
	day_of_week VARCHAR(30) NOT NULL, 
	CONSTRAINT schedules_pkey PRIMARY KEY (id), 
	CONSTRAINT schedules_course_id_fkey FOREIGN KEY(course_id) REFERENCES courses (id)
)

;
