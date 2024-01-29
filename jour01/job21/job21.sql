USE LaPlateforme;
-- Compter le nombre d'étudiants entre 18 et 25 ans
SELECT COUNT(*) AS nombre_etudiants_mineurs FROM etudiant WHERE age BETWEEN 18 AND 25;