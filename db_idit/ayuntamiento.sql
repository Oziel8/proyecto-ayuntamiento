-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-04-2022 a las 04:26:02
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ayuntamiento`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `1.solicitud`
--

CREATE TABLE `1.solicitud` (
  `idsolicitud` int(11) NOT NULL,
  `solicitud` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `2.acreditacion`
--

CREATE TABLE `2.acreditacion` (
  `idacreditacion` int(11) NOT NULL,
  `document` blob NOT NULL,
  `idtipo_titulo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `3.acta_constitutiva`
--

CREATE TABLE `3.acta_constitutiva` (
  `idacta_constitutiva` int(11) NOT NULL,
  `acta` blob NOT NULL,
  `idaplicable` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `4.identificacion`
--

CREATE TABLE `4.identificacion` (
  `ididentificacion` int(11) NOT NULL,
  `identificacion_pdf` blob NOT NULL,
  `idtipo_de_identificacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `5.ubicacion`
--

CREATE TABLE `5.ubicacion` (
  `idubicacion` int(11) NOT NULL,
  `ubicacion_pdf` blob NOT NULL,
  `link_ubi` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `6.plano`
--

CREATE TABLE `6.plano` (
  `idplano` int(11) NOT NULL,
  `plano_pdf` blob NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `7.carta_poder`
--

CREATE TABLE `7.carta_poder` (
  `idcarta_poder` int(11) NOT NULL,
  `cartapoder_pdf` blob DEFAULT NULL,
  `id_aplicable` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `aplicable`
--

CREATE TABLE `aplicable` (
  `idaplicable` int(11) NOT NULL,
  `descripcion` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estatus`
--

CREATE TABLE `estatus` (
  `idestatus` int(11) NOT NULL,
  `estatus` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `expediente`
--

CREATE TABLE `expediente` (
  `idExpediente` int(11) NOT NULL,
  `idsolicitud` int(11) NOT NULL,
  `idacreditacion` int(11) NOT NULL,
  `idacta_constitutiva` int(11) DEFAULT NULL,
  `ididentificacion` int(11) NOT NULL,
  `idubicacion` int(11) NOT NULL,
  `idplano` int(11) NOT NULL,
  `idcarta_poder` int(11) DEFAULT NULL,
  `idestatus` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `privilegios`
--

CREATE TABLE `privilegios` (
  `idprivilegios` int(11) NOT NULL,
  `privilegio` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_de_identificacion`
--

CREATE TABLE `tipo_de_identificacion` (
  `idtipo_de_identificacion` int(11) NOT NULL,
  `descripcion` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_titularidad`
--

CREATE TABLE `tipo_titularidad` (
  `idtipo_titulo` int(11) NOT NULL,
  `descripcion_titulo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idusuario` int(11) NOT NULL,
  `user` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `idprivilegios` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `1.solicitud`
--
ALTER TABLE `1.solicitud`
  ADD PRIMARY KEY (`idsolicitud`);

--
-- Indices de la tabla `2.acreditacion`
--
ALTER TABLE `2.acreditacion`
  ADD PRIMARY KEY (`idacreditacion`),
  ADD KEY `idtipo_titulo_idx` (`idtipo_titulo`);

--
-- Indices de la tabla `3.acta_constitutiva`
--
ALTER TABLE `3.acta_constitutiva`
  ADD PRIMARY KEY (`idacta_constitutiva`),
  ADD KEY `idaplicable_idx` (`idaplicable`);

--
-- Indices de la tabla `4.identificacion`
--
ALTER TABLE `4.identificacion`
  ADD PRIMARY KEY (`ididentificacion`),
  ADD KEY `idtipo_de_identificacion_idx` (`idtipo_de_identificacion`);

--
-- Indices de la tabla `5.ubicacion`
--
ALTER TABLE `5.ubicacion`
  ADD PRIMARY KEY (`idubicacion`);

--
-- Indices de la tabla `6.plano`
--
ALTER TABLE `6.plano`
  ADD PRIMARY KEY (`idplano`);

--
-- Indices de la tabla `7.carta_poder`
--
ALTER TABLE `7.carta_poder`
  ADD PRIMARY KEY (`idcarta_poder`),
  ADD KEY `id_aplicable_idx` (`id_aplicable`);

--
-- Indices de la tabla `aplicable`
--
ALTER TABLE `aplicable`
  ADD PRIMARY KEY (`idaplicable`);

--
-- Indices de la tabla `estatus`
--
ALTER TABLE `estatus`
  ADD PRIMARY KEY (`idestatus`);

--
-- Indices de la tabla `expediente`
--
ALTER TABLE `expediente`
  ADD PRIMARY KEY (`idExpediente`),
  ADD KEY `idsolicitud_idx` (`idsolicitud`),
  ADD KEY `idacreditacion_idx` (`idacreditacion`),
  ADD KEY `idacta_constitutiva_idx` (`idacta_constitutiva`),
  ADD KEY `ididentificacion_idx` (`ididentificacion`),
  ADD KEY `idubicacion_idx` (`idubicacion`),
  ADD KEY `idplano_idx` (`idplano`),
  ADD KEY `idcarta_poder_idx` (`idcarta_poder`),
  ADD KEY `idestatus_idx` (`idestatus`);

--
-- Indices de la tabla `privilegios`
--
ALTER TABLE `privilegios`
  ADD PRIMARY KEY (`idprivilegios`);

--
-- Indices de la tabla `tipo_de_identificacion`
--
ALTER TABLE `tipo_de_identificacion`
  ADD PRIMARY KEY (`idtipo_de_identificacion`);

--
-- Indices de la tabla `tipo_titularidad`
--
ALTER TABLE `tipo_titularidad`
  ADD PRIMARY KEY (`idtipo_titulo`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idusuario`),
  ADD KEY `idprivilegios_idx` (`idprivilegios`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `2.acreditacion`
--
ALTER TABLE `2.acreditacion`
  MODIFY `idacreditacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `3.acta_constitutiva`
--
ALTER TABLE `3.acta_constitutiva`
  MODIFY `idacta_constitutiva` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `4.identificacion`
--
ALTER TABLE `4.identificacion`
  MODIFY `ididentificacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `5.ubicacion`
--
ALTER TABLE `5.ubicacion`
  MODIFY `idubicacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `6.plano`
--
ALTER TABLE `6.plano`
  MODIFY `idplano` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `7.carta_poder`
--
ALTER TABLE `7.carta_poder`
  MODIFY `idcarta_poder` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `aplicable`
--
ALTER TABLE `aplicable`
  MODIFY `idaplicable` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estatus`
--
ALTER TABLE `estatus`
  MODIFY `idestatus` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `expediente`
--
ALTER TABLE `expediente`
  MODIFY `idExpediente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `privilegios`
--
ALTER TABLE `privilegios`
  MODIFY `idprivilegios` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_de_identificacion`
--
ALTER TABLE `tipo_de_identificacion`
  MODIFY `idtipo_de_identificacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_titularidad`
--
ALTER TABLE `tipo_titularidad`
  MODIFY `idtipo_titulo` int(11) NOT NULL AUTO_INCREMENT;


--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `2.acreditacion`
--
ALTER TABLE `2.acreditacion`
  ADD CONSTRAINT `idtipo_titulo` FOREIGN KEY (`idtipo_titulo`) REFERENCES `tipo_titularidad` (`idtipo_titulo`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `3.acta_constitutiva`
--
ALTER TABLE `3.acta_constitutiva`
  ADD CONSTRAINT `idaplicable` FOREIGN KEY (`idaplicable`) REFERENCES `aplicable` (`idaplicable`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `4.identificacion`
--
ALTER TABLE `4.identificacion`
  ADD CONSTRAINT `idtipo_de_identificacion` FOREIGN KEY (`idtipo_de_identificacion`) REFERENCES `tipo_de_identificacion` (`idtipo_de_identificacion`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `7.carta_poder`
--
ALTER TABLE `7.carta_poder`
  ADD CONSTRAINT `id_aplicable` FOREIGN KEY (`id_aplicable`) REFERENCES `aplicable` (`idaplicable`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `expediente`
--
ALTER TABLE `expediente`
  ADD CONSTRAINT `idacreditacion` FOREIGN KEY (`idacreditacion`) REFERENCES `2.acreditacion` (`idacreditacion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `idacta_constitutiva` FOREIGN KEY (`idacta_constitutiva`) REFERENCES `3.acta_constitutiva` (`idacta_constitutiva`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `idcarta_poder` FOREIGN KEY (`idcarta_poder`) REFERENCES `7.carta_poder` (`idcarta_poder`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `idestatus` FOREIGN KEY (`idestatus`) REFERENCES `estatus` (`idestatus`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `ididentificacion` FOREIGN KEY (`ididentificacion`) REFERENCES `4.identificacion` (`ididentificacion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `idplano` FOREIGN KEY (`idplano`) REFERENCES `6.plano` (`idplano`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `idsolicitud` FOREIGN KEY (`idsolicitud`) REFERENCES `1.solicitud` (`idsolicitud`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `idubicacion` FOREIGN KEY (`idubicacion`) REFERENCES `5.ubicacion` (`idubicacion`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `idprivilegios` FOREIGN KEY (`idprivilegios`) REFERENCES `privilegios` (`idprivilegios`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

--
-- Insertar datos a tabla `privilegios`
--

  INSERT INTO privilegios (privilegio) 
  VALUES ('alto'),('medio'),('bajo');

--
-- Insertar datos a tabla `aplicable`
--

  INSERT INTO aplicable (descripcion)
  VALUES ('no aplica');

--
-- Insertar datos a la tabla `tipo_titularidad`
--

  INSERT INTO tipo_titularidad (descripcion_titulo)
  VALUES ('Copia de los documentos donde se identifiquen los predios, fraccionamientos o lotes objeto de la regularización y los derechos de los promoventes respecto a los mismos'),
         ('La resolución de jurisdicción voluntaria o diligencia de apeo y deslinde'),
         ('La certificación de hechos ante Notario Público'),
         ('El acta circunstanciada de verificación de hechos suscrita por el Secretario General del Ayuntamiento'),
         ('El estudio y censo que realicen conjuntamente la Comisión y la Procuraduría'),
         ('El certificado de Inscripción del Registro Público'),
         ('La constancia del historial del predio como inmueble en propiedad privada'),
         ('Otros documentos legales idóneos');

--
-- Insertar datos a la tabla `tipo_de_identificacion`
--

  INSERT INTO tipo_de_identificacion (descripcion)
  VALUES ('INE');

--
-- Insertar datos a la tabla `estatus`

  INSERT INTO estatus (estatus)
  VALUES ('Finalizado');