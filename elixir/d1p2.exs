defmodule FuelGauge do
  def fuel_mass(mass) when mass > 0 do
    result = div(mass, 3) - 2
    max(result, 0) + fuel_mass(result)
  end

  def fuel_mass(_), do: 0
end

solution =
  File.read!("./data/d1.txt")
  |> String.split("\n")
  |> Enum.map(&String.to_integer/1)
  |> Enum.map(&FuelGauge.fuel_mass/1)
  |> Enum.sum()

IO.inspect(solution)
