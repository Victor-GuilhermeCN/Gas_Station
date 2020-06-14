-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 15-Jun-2020 às 01:00
-- Versão do servidor: 10.4.11-MariaDB
-- versão do PHP: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `fuelpump`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `client`
--

CREATE TABLE `client` (
  `cpf` varchar(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(9) NOT NULL,
  `points_fidelity` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `client`
--

INSERT INTO `client` (`cpf`, `name`, `phone`, `points_fidelity`) VALUES
('11374456879', 'Victor', '998035784', '106.20'),
('12312312311', 'Jonh', '999919839', '12.60'),
('12312312366', 'Alex', '99', NULL),
('12312312376', 'Pedro', '998877665', NULL),
('12312312398', 'John', '998765431', NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `nf`
--

CREATE TABLE `nf` (
  `id_nf` int(10) NOT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `nf_value` decimal(10,2) NOT NULL,
  `nf_item` varchar(255) NOT NULL,
  `nf_amount` decimal(10,2) DEFAULT NULL,
  `date_nf` date DEFAULT NULL,
  `nf_hour` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `nf`
--

INSERT INTO `nf` (`id_nf`, `cpf`, `nf_value`, `nf_item`, `nf_amount`, `date_nf`, `nf_hour`) VALUES
(23, '11374456879', '82.00', 'Gasoline', '24.00', '2020-06-14', '01:04:48'),
(25, '12312312311', '24.00', 'Gasoline', '7.06', '2020-06-14', '01:06:52'),
(27, NULL, '24.00', 'Gasoline', '7.06', '2020-06-14', '01:11:12'),
(28, NULL, '130.00', 'Gasoline', '38.24', '2020-06-14', '01:11:45'),
(29, NULL, '44.00', 'Gasoline', '13.00', '2020-06-14', '01:12:22'),
(30, NULL, '102.00', 'Gasoline', '30.00', '2020-06-14', '04:46:25'),
(31, '11374456879', '30.00', 'Gasoline', '8.82', '2020-06-14', '16:28:48'),
(32, NULL, '38.30', 'Gasoline', '11.26', '2020-06-14', '16:29:46'),
(33, '11374456879', '130.00', 'Gasoline', '38.30', '2020-06-14', '16:35:17'),
(34, '11374456879', '130.00', 'Gasoline', '38.30', '2020-06-14', '16:35:40'),
(35, '11374456879', '130.00', 'Gasoline', '38.30', '2020-06-14', '16:36:37'),
(36, '11374456879', '130.00', 'Gasoline', '38.30', '2020-06-14', '16:37:18'),
(37, '11374456879', '130.00', 'Gasoline', '38.00', '2020-06-14', '16:38:30'),
(38, '11374456879', '130.00', 'Gasoline', '38.30', '2020-06-14', '16:38:42'),
(39, '11374456879', '130.00', 'Gasoline', '38.30', '2020-06-14', '16:38:57'),
(40, NULL, '30.50', 'Gasoline', '8.97', '2020-06-14', '16:46:09'),
(41, NULL, '32.00', 'Gasoline', '9.41', '2020-06-14', '16:50:18'),
(42, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '16:55:40'),
(45, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '16:57:02'),
(46, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '16:57:26'),
(47, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '16:57:41'),
(49, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '17:02:47'),
(50, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '17:09:18'),
(51, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '17:09:41'),
(52, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '17:09:56'),
(53, NULL, '30.00', 'Gas', '10.00', '2020-06-14', '17:14:10'),
(54, '11812312344', '30.00', 'Gas', '10.00', '2020-06-14', '17:15:22'),
(55, '11812312344', '30.00', 'Gas', '10.00', '2020-06-14', '18:06:51'),
(56, NULL, '39.00', 'Gasoline Adtiv', '10.00', '2020-06-14', '18:10:07'),
(57, NULL, '34.00', 'Gasoline', '10.00', '2020-06-14', '18:13:15'),
(58, '11374456879', '30.00', 'Gasoline', '8.82', '2020-06-14', '18:21:59'),
(59, '11374456879', '10.00', 'Gasoline', '2.94', '2020-06-14', '18:22:38');

-- --------------------------------------------------------

--
-- Estrutura da tabela `tank`
--

CREATE TABLE `tank` (
  `id_comb` int(10) NOT NULL,
  `name_comb` varchar(255) NOT NULL,
  `qt_comb` decimal(10,2) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tank`
--

INSERT INTO `tank` (`id_comb`, `name_comb`, `qt_comb`, `price`) VALUES
(1, 'Gasoline', '52.87', '3.40'),
(2, 'Gas', '300.00', '2.20'),
(3, 'Diesel', '150.00', '3.23'),
(4, 'Alcohol', '200.00', '3.24'),
(5, 'Gasoline Adtiv', '190.00', '3.89'),
(6, 'Alcohol - F', '200.00', '3.60');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`cpf`);

--
-- Índices para tabela `nf`
--
ALTER TABLE `nf`
  ADD PRIMARY KEY (`id_nf`);

--
-- Índices para tabela `tank`
--
ALTER TABLE `tank`
  ADD PRIMARY KEY (`id_comb`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `nf`
--
ALTER TABLE `nf`
  MODIFY `id_nf` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT de tabela `tank`
--
ALTER TABLE `tank`
  MODIFY `id_comb` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
