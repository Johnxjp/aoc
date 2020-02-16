input = File.read!("./data/d2.txt") |> String.split(",") |> Enum.map(&String.to_integer/1)
input = List.replace_at(input, 1, 12)
input = List.replace_at(input, 2, 2)

defmodule GravityAssist do
  defp operate(list, []) do
    list
  end

  defp operate(list, [99 | _]) do
    list
  end

  defp operate(list, [1 | tail]) do
    [a, b, store | remainder] = tail
    val_a = Enum.at(list, a)
    val_b = Enum.at(list, b)
    list = List.replace_at(list, store, val_a + val_b)
    operate(list, remainder)
  end

  defp operate(list, [2 | tail]) do
    [a, b, store | remainder] = tail
    val_a = Enum.at(list, a)
    val_b = Enum.at(list, b)
    list = List.replace_at(list, store, val_a * val_b)
    operate(list, remainder)
  end

  def parse(list) do
    operate(list, list)
  end
end

output = GravityAssist.parse(input)
IO.inspect(hd(output))
