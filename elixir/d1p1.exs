fuel_mass = fn mass -> div(mass, 3) - 2 end

solution =
  File.read!("./data/d1.txt")
  |> String.split("\n")
  |> Enum.map(&String.to_integer/1)
  |> Enum.map(fuel_mass)
  |> Enum.sum()

IO.inspect(solution)
