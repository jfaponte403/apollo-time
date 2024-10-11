
CREATE TABLE classrooms (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	type VARCHAR(50) NOT NULL, 
	capacity INTEGER NOT NULL, 
	CONSTRAINT classrooms_pkey PRIMARY KEY (id)
)

;
INSERT INTO classrooms VALUES ('C101', 'Room A', 'Lecture', 50);
INSERT INTO classrooms VALUES ('C102', 'Room B', 'Laboratory', 30);
INSERT INTO classrooms VALUES ('C103', 'Room C', 'Lecture', 100);

CREATE TABLE degrees (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	CONSTRAINT degrees_pkey PRIMARY KEY (id)
)

;
INSERT INTO degrees VALUES ('D01', 'Computer Science');
INSERT INTO degrees VALUES ('D02', 'Mathematics');
INSERT INTO degrees VALUES ('D03', 'Physics');
INSERT INTO degrees VALUES ('2e523f82-c01b-47e5-a200-1edf33f760b0', '9 - A');
INSERT INTO degrees VALUES ('6f7229cd-d435-40e5-9cf5-1cb1a299c076', 'test');
INSERT INTO degrees VALUES ('a3d540ff-420a-465a-aed7-650beea341af', 'Noveno A');
INSERT INTO degrees VALUES ('b5250d47-3a9d-49d5-986b-57f05ba19235', 'DECIMO A');
INSERT INTO degrees VALUES ('90b6f27d-fa77-4efb-9f7c-c37a1edf0796', 'SEPTIMO B');
INSERT INTO degrees VALUES ('4a5d3e04-3d2d-4999-ae84-fd0dfbabc5e5', 'ONCE A');

CREATE TABLE roles (
	id VARCHAR NOT NULL, 
	rol VARCHAR NOT NULL, 
	CONSTRAINT roles_pkey PRIMARY KEY (id)
)

;
INSERT INTO roles VALUES ('02', 'teacher');
INSERT INTO roles VALUES ('01', 'admin');
INSERT INTO roles VALUES ('03', 'student');

CREATE TABLE subjects (
	id VARCHAR NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	CONSTRAINT subjects_pkey PRIMARY KEY (id)
)

;
INSERT INTO subjects VALUES ('S101', 'Data Structures');
INSERT INTO subjects VALUES ('S102', 'Calculus I');
INSERT INTO subjects VALUES ('S103', 'Quantum Mechanics');

CREATE TABLE users (
	id VARCHAR NOT NULL, 
	role_id VARCHAR NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	email VARCHAR(100) NOT NULL, 
	phone_number VARCHAR(15) NOT NULL, 
	CONSTRAINT users_pkey PRIMARY KEY (id), 
	CONSTRAINT users_role_id_fkey FOREIGN KEY(role_id) REFERENCES roles (id) ON DELETE CASCADE
)

;
INSERT INTO users VALUES ('0c2dcfdf-a979-4b9d-ad43-130e6535080f', '02', 'John Doe', 'johndoe@example.com', '1234567890');
INSERT INTO users VALUES ('c0a4a752-dab0-482e-9829-c75505564558', '02', 'John1', 'johndoe@example.com', '1234567890');
INSERT INTO users VALUES ('897ff68f-242f-4dba-8dd9-76c1ab54eb18', '02', 'student', 'student@student.com', '3006049461');
INSERT INTO users VALUES ('c9f69903-6ee4-44c4-9442-699285247818', '02', 'student', 'student@student.com', '3006049461');
INSERT INTO users VALUES ('874024e9-7677-4ca7-abe8-d95d502d5150', '02', 'student', 'student@student.com', '3006049461');
INSERT INTO users VALUES ('234ea457-d731-49c4-a849-bd89f126d77c', '02', 'student', 'student@student.com', '3006049461');
INSERT INTO users VALUES ('001', '01', 'jhonattan', 'jfaponte@udistrital.com', '3006046460');
INSERT INTO users VALUES ('4fc14354-7469-470d-a829-20e4050b148e', '02', 'John4', 'johndoe@example.com', '1234567890');
INSERT INTO users VALUES ('06a235f5-815f-4fbe-8f6d-6efa2e2e41ef', '02', 'John4', 'johndoe@example.com', '1234567890');
INSERT INTO users VALUES ('54f7f094-96e1-46ef-a338-d18bf8d0eb33', '02', 'John4', 'johndoe@example.com', '1234567890');
INSERT INTO users VALUES ('177241a5-4a7a-4c4c-a5ff-e58eb793f8f3', '02', 'Alfredo', 'johndoe@example.com', '1234567890');
INSERT INTO users VALUES ('f0f42660-87c1-473c-a9a7-afa74622d16c', '02', 'Test', 'test@test.com', '12312');
INSERT INTO users VALUES ('4e57ab07-5a85-493a-a7c4-9e1116b70c52', '02', 'aaa', 'aa@aaa.com', '12342134');
INSERT INTO users VALUES ('2a2ce2c5-6822-4366-b0c0-41f537af17a0', '02', 'Alfredo2', 'Aldf2@gmail.com', '12312');
INSERT INTO users VALUES ('ade60991-2e07-4753-8afc-5be518b50960', '02', 'Quiles', 'QuilesF@udistrital.edu.co', '12312');
INSERT INTO users VALUES ('20fd254c-8de1-4f47-83bb-c39d4bd88cfd', '02', 'student', 'student@student.com', '3006049461');
INSERT INTO users VALUES ('fabae481-1fe0-4856-b362-6e720e342015', '02', 'Andres', 'Aldf2@gmail.com', '123123');
INSERT INTO users VALUES ('2789898b-9bea-4cdf-afa1-f0d83f44c776', '02', 'Andres Llinas', 'Andres@gmail.com', '3122233322');

CREATE TABLE admins (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	CONSTRAINT admins_pkey PRIMARY KEY (id), 
	CONSTRAINT admins_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
)

;
INSERT INTO admins VALUES ('01', '001');

CREATE TABLE login (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	username VARCHAR(30) NOT NULL, 
	password VARCHAR(100) NOT NULL, 
	CONSTRAINT login_pkey PRIMARY KEY (id), 
	CONSTRAINT login_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
)

;
INSERT INTO login VALUES ('2e6587f0-850c-402b-a12a-642370b752e7', '0c2dcfdf-a979-4b9d-ad43-130e6535080f', 'john.johndoe', 'uppwBh3rwh');
INSERT INTO login VALUES ('3ea9b473-9c81-4c03-addc-f14bc94248d1', 'c0a4a752-dab0-482e-9829-c75505564558', 'john1.johndoe', 'yt36DbroSB');
INSERT INTO login VALUES ('4de7a320-9b7c-4bb3-bbce-49ca0cdbed1d', '234ea457-d731-49c4-a849-bd89f126d77c', 'student.student', 'nyDl76wIBh');
INSERT INTO login VALUES ('01', '001', 'admin', '1234');
INSERT INTO login VALUES ('5365134f-34df-469f-a057-d608d99be438', '4fc14354-7469-470d-a829-20e4050b148e', 'john4.johndoe', '5K9zEb0uT1');
INSERT INTO login VALUES ('d3e1acf7-2bd8-41c6-9cdd-a0094b86d632', '06a235f5-815f-4fbe-8f6d-6efa2e2e41ef', 'john4.johndoe', 'fWoPSqFTHr');
INSERT INTO login VALUES ('e855d74c-b734-4a6f-a26e-b90a71753c2c', '54f7f094-96e1-46ef-a338-d18bf8d0eb33', 'john4.johndoe', 'G2QcXYxD7s');
INSERT INTO login VALUES ('e1617388-d27a-4b42-bcd0-9f31c45c5f63', '177241a5-4a7a-4c4c-a5ff-e58eb793f8f3', 'alfredo.johndoe', 'Y81kAOYum6');
INSERT INTO login VALUES ('0a16c956-1d03-4941-808e-e0a90f0ca778', 'f0f42660-87c1-473c-a9a7-afa74622d16c', 'test.test', 'G2TY6xJlD8');
INSERT INTO login VALUES ('7ca6384b-62ad-463e-9a2d-f7af48772e60', '4e57ab07-5a85-493a-a7c4-9e1116b70c52', 'aaa.aa', 'D81meoeT9J');
INSERT INTO login VALUES ('27607808-c416-4c04-bbb7-23ee5c2f4f11', '2a2ce2c5-6822-4366-b0c0-41f537af17a0', 'alfredo2.Aldf2', 'tDEsAnF1E3');
INSERT INTO login VALUES ('dcbd7df2-dfbc-4a7d-a0fa-4615328dc813', 'ade60991-2e07-4753-8afc-5be518b50960', 'quiles.QuilesF', 'OaHiQydUBO');
INSERT INTO login VALUES ('33563a09-3299-4465-bdf7-1df79770e600', '20fd254c-8de1-4f47-83bb-c39d4bd88cfd', 'student.student', 'Vhw3fOVAKJ');
INSERT INTO login VALUES ('72d00671-d892-474e-9c28-7e7ffc2bf1a3', 'fabae481-1fe0-4856-b362-6e720e342015', 'andres.Aldf2', 'JovamUjxka');
INSERT INTO login VALUES ('ae7a353e-e7ee-413c-9803-f438d1beadd4', '2789898b-9bea-4cdf-afa1-f0d83f44c776', 'andres.Andres', '2t4hdxKL6Q');

CREATE TABLE students (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	degree_id VARCHAR NOT NULL, 
	gpa DOUBLE PRECISION NOT NULL, 
	CONSTRAINT students_pkey PRIMARY KEY (id), 
	CONSTRAINT students_degree_id_fkey FOREIGN KEY(degree_id) REFERENCES degrees (id) ON DELETE CASCADE, 
	CONSTRAINT students_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
)

;
INSERT INTO students VALUES ('ST01', '0c2dcfdf-a979-4b9d-ad43-130e6535080f', 'D01', 3.8);
INSERT INTO students VALUES ('ST02', 'c0a4a752-dab0-482e-9829-c75505564558', 'D02', 3.6);
INSERT INTO students VALUES ('7bebebf5-d59c-45e6-a4bb-1ead52bebd63', '234ea457-d731-49c4-a849-bd89f126d77c', 'D02', 45.0);
INSERT INTO students VALUES ('19a55670-7fc5-4e1d-a2a7-103d2dd21290', '20fd254c-8de1-4f47-83bb-c39d4bd88cfd', 'D02', 45.0);
INSERT INTO students VALUES ('2e491344-3599-4c3b-860e-364c3f52d066', 'fabae481-1fe0-4856-b362-6e720e342015', '6f7229cd-d435-40e5-9cf5-1cb1a299c076', 32.0);
INSERT INTO students VALUES ('e6d9949c-de3c-4339-b4e0-d5881fa7af17', '2789898b-9bea-4cdf-afa1-f0d83f44c776', '90b6f27d-fa77-4efb-9f7c-c37a1edf0796', 50.0);

CREATE TABLE teachers (
	id VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	salary DOUBLE PRECISION NOT NULL, 
	specialization VARCHAR(100) NOT NULL, 
	CONSTRAINT teachers_pkey PRIMARY KEY (id), 
	CONSTRAINT teachers_user_id_fkey FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
)

;
INSERT INTO teachers VALUES ('09a11b97-48bf-44e8-bccc-fb7981ee92e4', '4fc14354-7469-470d-a829-20e4050b148e', 12000.0, 'math');
INSERT INTO teachers VALUES ('71400c2c-51fe-4b16-965a-498357e227cf', '06a235f5-815f-4fbe-8f6d-6efa2e2e41ef', 12000.0, 'math');
INSERT INTO teachers VALUES ('dcb8454d-d704-4c0a-99c3-2a4d7cec6431', '54f7f094-96e1-46ef-a338-d18bf8d0eb33', 12000.0, 'math');
INSERT INTO teachers VALUES ('54d92b70-6ec6-4f72-86ac-11e5b45a0ad2', '177241a5-4a7a-4c4c-a5ff-e58eb793f8f3', 12000.0, 'math');
INSERT INTO teachers VALUES ('5555b387-ae55-4141-804a-426320abe152', 'f0f42660-87c1-473c-a9a7-afa74622d16c', 123123.0, 'asdsad');
INSERT INTO teachers VALUES ('fbe09f4c-7fed-47fc-aada-4e4c08bfe580', '4e57ab07-5a85-493a-a7c4-9e1116b70c52', 123.0, 'aaaa');
INSERT INTO teachers VALUES ('694708ba-bfd0-403e-b1c4-960e519b7eb5', '2a2ce2c5-6822-4366-b0c0-41f537af17a0', 12123213.0, 'assdsd');
INSERT INTO teachers VALUES ('1f61305c-384b-4ea9-aa83-ee16a1612de2', 'ade60991-2e07-4753-8afc-5be518b50960', 123412.0, 'asdasd');

CREATE TABLE courses (
	id VARCHAR NOT NULL, 
	classroom_id VARCHAR NOT NULL, 
	subject_id VARCHAR NOT NULL, 
	degrees_id VARCHAR NOT NULL, 
	teacher_id VARCHAR NOT NULL, 
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
	CONSTRAINT schedules_pkey PRIMARY KEY (id), 
	CONSTRAINT schedules_course_id_fkey FOREIGN KEY(course_id) REFERENCES courses (id) ON DELETE CASCADE
)

;
