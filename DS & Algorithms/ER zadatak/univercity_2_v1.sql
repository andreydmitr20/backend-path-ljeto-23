-- building definition

CREATE TABLE building (
	id_building INTEGER PRIMARY KEY AUTOINCREMENT,
	address TEXT,
	label TEXT
);


-- professor definition

CREATE TABLE professor (
	id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
	jmbg TEXT,
	name TEXT,
	date_of_birth TEXT,
	title TEXT,
	speciality TEXT
);


-- faculty definition

CREATE TABLE faculty (
	id_faculty INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	phone TEXT,
	dekan_id_professor INTEGER,
	CONSTRAINT faculty_FK FOREIGN KEY (dekan_id_professor) REFERENCES professor(id_professor)
);


-- postgraduate definition

CREATE TABLE postgraduate (
	id_postgraduate INTEGER PRIMARY KEY AUTOINCREMENT,
	jmbg TEXT,
	name TEXT,
	date_of_birth TEXT,
	direction TEXT,
	id_faculty INTEGER,
	advisor_id_postgraduate INTEGER,
	CONSTRAINT postgraduate_FK FOREIGN KEY (id_faculty) REFERENCES faculty(id_faculty),
	CONSTRAINT postgraduate_FK_advisor FOREIGN KEY (advisor_id_postgraduate) REFERENCES postgraduate(id_postgraduate)
);


-- professor_faculty definition

CREATE TABLE professor_faculty (
	id_professor INTEGER,
	id_faculty INTEGER, lessons_time TEXT,
	CONSTRAINT professor_faculty_FK FOREIGN KEY (id_professor) REFERENCES professor(id_professor),
	CONSTRAINT professor_faculty_FK_1 FOREIGN KEY (id_faculty) REFERENCES faculty(id_faculty)
);


-- project definition

CREATE TABLE project (
	id_project INTEGER PRIMARY KEY AUTOINCREMENT,
	sponsor_name TEXT,
	"number" TEXT,
	start_date TEXT,
	end_date TEXT,
	budget REAL,
	supervisor_id_professsor INTEGER,
	CONSTRAINT project_FK FOREIGN KEY (supervisor_id_professsor) REFERENCES professor(id_professor)
);


-- project_postgraduate definition

CREATE TABLE project_postgraduate (
	id_project INTEGER,
	id_postgraduate INTEGER,
	mentor_id_professor INTEGER,
	CONSTRAINT project_postgraduate_FK FOREIGN KEY (mentor_id_professor) REFERENCES professor(id_professor),
	CONSTRAINT project_postgraduate_FK_1 FOREIGN KEY (id_project) REFERENCES project(id_project),
	CONSTRAINT project_postgraduate_FK_2 FOREIGN KEY (id_postgraduate) REFERENCES postgraduate(id_postgraduate)
);


-- project_professor definition

CREATE TABLE "project_professor" (
	id_professor INTEGER,
	id_project INTEGER,
	lead INTEGER,
	CONSTRAINT project_group_FK FOREIGN KEY (id_project) REFERENCES project(id_project),
	CONSTRAINT project_group_FK_1 FOREIGN KEY (id_professor) REFERENCES professor(id_professor)
);


-- building_faculty definition

CREATE TABLE building_faculty (
	id_building INTEGER,
	id_faculty INTEGER,
	CONSTRAINT building_faculty_FK FOREIGN KEY (id_faculty) REFERENCES faculty(id_faculty),
	CONSTRAINT building_faculty_FK_1 FOREIGN KEY (id_building) REFERENCES building(id_building)
);
