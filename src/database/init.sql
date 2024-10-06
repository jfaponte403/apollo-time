
CREATE TABLE classrooms (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	type VARCHAR(50) NOT NULL, 
	capacity INTEGER NOT NULL, 
	CONSTRAINT classrooms_pkey PRIMARY KEY (id)
)

;
INSERT INTO classrooms VALUES ('123e4567-e89b-12d3-a456-426614174000', 'Classroom A', 'Lecture', 30);
INSERT INTO classrooms VALUES ('223e4567-e89b-12d3-a456-426614174001', 'Classroom B', 'Lab', 25);
INSERT INTO classrooms VALUES ('323e4567-e89b-12d3-a456-426614174002', 'Classroom C', 'Seminar', 20);

CREATE TABLE degrees (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	CONSTRAINT degrees_pkey PRIMARY KEY (id)
)

;
INSERT INTO degrees VALUES ('423e4567-e89b-12d3-a456-426614174003', 'Computer Science');
INSERT INTO degrees VALUES ('523e4567-e89b-12d3-a456-426614174004', 'Mathematics');
INSERT INTO degrees VALUES ('623e4567-e89b-12d3-a456-426614174005', 'Biology');

CREATE TABLE roles (
	id VARCHAR NOT NULL, 
	rol VARCHAR NOT NULL, 
	CONSTRAINT roles_pkey PRIMARY KEY (id)
)

;
INSERT INTO roles VALUES ('723e4567-e89b-12d3-a456-426614174006', 'Admin');
INSERT INTO roles VALUES ('823e4567-e89b-12d3-a456-426614174007', 'Teacher');
INSERT INTO roles VALUES ('923e4567-e89b-12d3-a456-426614174008', 'Student');

CREATE TABLE subjects (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	CONSTRAINT subjects_pkey PRIMARY KEY (id)
)

;
INSERT INTO subjects VALUES ('a23e4567-e89b-12d3-a456-426614174009', 'Databases');
INSERT INTO subjects VALUES ('b23e4567-e89b-12d3-a456-426614174010', 'Algorithms');
INSERT INTO subjects VALUES ('c23e4567-e89b-12d3-a456-426614174011', 'Operating Systems');

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
INSERT INTO users VALUES ('d23e4567-e89b-12d3-a456-426614174012', '723e4567-e89b-12d3-a456-426614174006', 'Alice Johnson', 'alice@example.com', '555-0101');
INSERT INTO users VALUES ('e23e4567-e89b-12d3-a456-426614174013', '823e4567-e89b-12d3-a456-426614174007', 'Bob Smith', 'bob@example.com', '555-0102');
INSERT INTO users VALUES ('f23e4567-e89b-12d3-a456-426614174014', '923e4567-e89b-12d3-a456-426614174008', 'Charlie Brown', 'charlie@example.com', '555-0103');

CREATE TABLE admins (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	CONSTRAINT admins_pkey PRIMARY KEY (id), 
	CONSTRAINT admins_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id)
)

;
INSERT INTO admins VALUES ('g23e4567-e89b-12d3-a456-426614174015', 'd23e4567-e89b-12d3-a456-426614174012');
INSERT INTO admins VALUES ('h23e4567-e89b-12d3-a456-426614174016', 'e23e4567-e89b-12d3-a456-426614174013');
INSERT INTO admins VALUES ('i23e4567-e89b-12d3-a456-426614174017', 'f23e4567-e89b-12d3-a456-426614174014');

CREATE TABLE login (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(100) NOT NULL, 
	CONSTRAINT login_pkey PRIMARY KEY (id), 
	CONSTRAINT login_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id)
)

;
INSERT INTO login VALUES ('j23e4567-e89b-12d3-a456-426614174018', 'd23e4567-e89b-12d3-a456-426614174012', 'admin', '1234');
INSERT INTO login VALUES ('k23e4567-e89b-12d3-a456-426614174019', 'e23e4567-e89b-12d3-a456-426614174013', 'teacher', '1234');
INSERT INTO login VALUES ('l23e4567-e89b-12d3-a456-426614174020', 'f23e4567-e89b-12d3-a456-426614174014', 'student', '1234');

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
INSERT INTO students VALUES ('m23e4567-e89b-12d3-a456-426614174021', 'f23e4567-e89b-12d3-a456-426614174014', '423e4567-e89b-12d3-a456-426614174003', 3.5);
INSERT INTO students VALUES ('n23e4567-e89b-12d3-a456-426614174022', 'd23e4567-e89b-12d3-a456-426614174012', '523e4567-e89b-12d3-a456-426614174004', 3.8);
INSERT INTO students VALUES ('o23e4567-e89b-12d3-a456-426614174023', 'e23e4567-e89b-12d3-a456-426614174013', '623e4567-e89b-12d3-a456-426614174005', 3.2);

CREATE TABLE teachers (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	salary DOUBLE PRECISION NOT NULL, 
	specialization VARCHAR(100) NOT NULL, 
	CONSTRAINT teachers_pkey PRIMARY KEY (id), 
	CONSTRAINT teachers_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id)
)

;
INSERT INTO teachers VALUES ('p23e4567-e89b-12d3-a456-426614174024', 'e23e4567-e89b-12d3-a456-426614174013', 60000.0, 'Computer Science');
INSERT INTO teachers VALUES ('q23e4567-e89b-12d3-a456-426614174025', 'd23e4567-e89b-12d3-a456-426614174012', 65000.0, 'Mathematics');
INSERT INTO teachers VALUES ('r23e4567-e89b-12d3-a456-426614174026', 'f23e4567-e89b-12d3-a456-426614174014', 55000.0, 'Biology');

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
INSERT INTO courses VALUES ('s23e4567-e89b-12d3-a456-426614174027', '123e4567-e89b-12d3-a456-426614174000', 'a23e4567-e89b-12d3-a456-426614174009', '423e4567-e89b-12d3-a456-426614174003', 'p23e4567-e89b-12d3-a456-426614174024');
INSERT INTO courses VALUES ('t23e4567-e89b-12d3-a456-426614174028', '223e4567-e89b-12d3-a456-426614174001', 'b23e4567-e89b-12d3-a456-426614174010', '523e4567-e89b-12d3-a456-426614174004', 'q23e4567-e89b-12d3-a456-426614174025');
INSERT INTO courses VALUES ('u23e4567-e89b-12d3-a456-426614174029', '323e4567-e89b-12d3-a456-426614174002', 'c23e4567-e89b-12d3-a456-426614174011', '623e4567-e89b-12d3-a456-426614174005', 'r23e4567-e89b-12d3-a456-426614174026');

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
INSERT INTO schedules VALUES ('v23e4567-e89b-12d3-a456-426614174030', 's23e4567-e89b-12d3-a456-426614174027', '09:00', '10:30', 'Monday');
INSERT INTO schedules VALUES ('w23e4567-e89b-12d3-a456-426614174031', 't23e4567-e89b-12d3-a456-426614174028', '11:00', '12:30', 'Wednesday');
INSERT INTO schedules VALUES ('x23e4567-e89b-12d3-a456-426614174032', 'u23e4567-e89b-12d3-a456-426614174029', '13:00', '14:30', 'Friday');
