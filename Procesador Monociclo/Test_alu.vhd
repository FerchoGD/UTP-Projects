--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   16:37:35 10/06/2016
-- Design Name:   
-- Module Name:   C:/Users/utp.CRIE/Desktop/sparcv8-monocicle/Test_alu.vhd
-- Project Name:  monocicle-sparcv8
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: alu
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY Test_alu IS
END Test_alu;
 
ARCHITECTURE behavior OF Test_alu IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT alu
    PORT(
         aluop : IN  std_logic_vector(5 downto 0);
         crs1 : IN  std_logic_vector(31 downto 0);
         crs2 : IN  std_logic_vector(31 downto 0);
         r : OUT  std_logic_vector(31 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal aluop : std_logic_vector(5 downto 0) := (others => '0');
   signal crs1 : std_logic_vector(31 downto 0) := (others => '0');
   signal crs2 : std_logic_vector(31 downto 0) := (others => '0');

 	--Outputs
   signal r : std_logic_vector(31 downto 0);
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
 
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: alu PORT MAP (
          aluop => aluop,
          crs1 => crs1,
          crs2 => crs2,
          r => r
        );

  

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
		crs1 <= x"00000005";
		crs2 <= x"00000004";
		aluop<= "000000";
      wait for 100 ns;
		aluop<= "000001";
      wait for 100 ns;
		aluop<= "000010";
      wait for 100 ns;
		aluop<= "000011";
      wait for 100 ns;
		aluop<= "000100";
      wait for 100 ns;
		aluop<= "000101";
      wait for 100 ns;
		aluop<= "000110";
      wait for 100 ns;
		aluop<= "000111";
      wait for 100 ns;

      -- insert stimulus here 

      wait;
   end process;

END;
