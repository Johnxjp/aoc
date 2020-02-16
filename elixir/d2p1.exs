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

input = File.read!("./data/d2.txt") |> String.split(",") |> Enum.map(&String.to_integer/1)
input = List.replace_at(input, 1, 12)
input = List.replace_at(input, 2, 2)
output = GravityAssist.parse(input)
IO.inspect(hd(output))
