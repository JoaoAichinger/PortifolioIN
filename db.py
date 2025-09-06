import sqlite3


def get_db():
    path = 'database.db'
    conn = sqlite3.connect(path)
    return conn

    

def create_db():
    path = 'database.db'

    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    sql = '''
CREATE TABLE Usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('Recrutador', 'Aluno'))
);

CREATE TABLE Aluno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    celular TEXT,
    foto TEXT,
    descricao TEXT,
    curso TEXT NOT NULL CHECK (curso IN ('Design', 'Full Stack', 'Marketing', 'Fotografia')),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
        ON DELETE CASCADE
);

CREATE TABLE Projetos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER NOT NULL,
    tipo TEXT NOT NULL CHECK (tipo IN ('Foto', 'Vídeo', 'Código')),
    titulo TEXT NOT NULL,
    descricao TEXT,
    corpo TEXT NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES Aluno(id)
        ON DELETE CASCADE
);

CREATE TABLE Recrutador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    foto TEXT,
    empresa TEXT NOT NULL,
    descricao TEXT,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
        ON DELETE CASCADE
);
'''
    cursor.executescript(sql)
    conn.commit()
    conn.close()

