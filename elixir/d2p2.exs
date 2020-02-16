defmodule GravityAssist do
  defp parse(list, []), do: list
  defp parse(list, [99 | _]), do: list

  defp parse(list, [code | tail]) do
    [a, b, store | remainder] = tail
    [a, b] = [a, b] |> Enum.map(fn index -> Enum.at(list, index) end)

    func =
      case code do
        1 -> &+/2
        2 -> &*/2
      end

    list = List.replace_at(list, store, func.(a, b))
    parse(list, remainder)
  end

  def parse(list) do
    parse(list, list)
  end
end

defmodule Solver do
  defp permutations(noun_range, verb_range) do
    List.flatten(
      Enum.map(noun_range, fn a ->
        Enum.map(verb_range, fn b -> {a, b} end)
      end)
    )
  end

  defp solve(perms, input) do
    Enum.drop_while(perms, fn {noun, verb} ->
      new_input = List.replace_at(input, 1, noun)
      new_input = List.replace_at(new_input, 2, verb)
      output = GravityAssist.parse(new_input)
      hd(output) != 19_690_720
    end)
  end

  def solve(noun_range, verb_range, input) do
    perms = permutations(noun_range, verb_range)
    tried_values = solve(perms, input)
    List.first(tried_values)
  end
end

input = File.read!("./data/d2.txt") |> String.split(",") |> Enum.map(&String.to_integer/1)
{noun, verb} = Solver.solve(0..99, 0..99, input)
IO.inspect(100 * noun + verb)
