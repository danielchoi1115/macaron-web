-- Production 환경에서 *.* privilege는 위험하니 사용을 권장하지 않음

CREATE USER 'macaron'@'%' IDENTIFIED BY 'macaron';
GRANT all privileges ON *.* TO 'macaron'@'%';
FLUSH PRIVILEGES;
