USE LaPlateforme;
-- Récupérer les informations de l'étudiant le plus âgé
SELECT * FROM etudiant WHERE age = (SELECT MAX(age) FROM etudiant);
