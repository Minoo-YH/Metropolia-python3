-- create_flightgame.sql
CREATE DATABASE IF NOT EXISTS flightgame
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_general_ci;

USE flightgame;

CREATE TABLE IF NOT EXISTS airport (
  ident          VARCHAR(10)  NOT NULL,
  name           VARCHAR(255) NOT NULL,
  municipality   VARCHAR(255),
  iso_country    CHAR(2)      NOT NULL,
  type           VARCHAR(50)  NOT NULL,
  latitude_deg   DECIMAL(9,6) NOT NULL,
  longitude_deg  DECIMAL(9,6) NOT NULL,
  PRIMARY KEY (ident),
  INDEX idx_iso_country (iso_country),
  INDEX idx_type (type)
);

INSERT INTO airport (ident, name, municipality, iso_country, type, latitude_deg, longitude_deg) VALUES
('EFHK', 'Helsinki Vantaa Airport', 'Vantaa', 'FI', 'large_airport', 60.317200, 24.963300),
('EFKU', 'Kuopio Airport', 'Kuopio', 'FI', 'medium_airport', 63.007100, 27.797800),
('EGLL', 'London Heathrow Airport', 'London', 'GB', 'large_airport', 51.470000, -0.454300),
('ESSA', 'Stockholm Arlanda Airport', 'Sigtuna', 'SE', 'large_airport', 59.651900, 17.918600),
('OIIE', 'Imam Khomeini International', 'Tehran', 'IR', 'large_airport', 35.416100, 51.152200),
('OIAM', 'Mahshahr Airport', 'Mahshahr', 'IR', 'medium_airport', 30.556200, 49.151900),
('OIHH', 'Hamadan Airport', 'Hamadan', 'IR', 'small_airport', 34.869200, 48.552500),
('EFHE', 'Helsinki Heliport (Demo)', 'Helsinki', 'FI', 'heliport', 60.170000, 24.940000);
