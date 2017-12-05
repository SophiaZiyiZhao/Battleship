defmodule Battleship.Game.Posn do
  alias Battleship.Game
  alias Battleship.Game.Posn

  defstruct [:x, :y]

  def new(x, y) do 
    if x >= 0 && x < Game.board_grid && y >= 0 && y < Game.board_grid do
      {:ok, %Posn{x: x, y: y}}
    else
      {:error, :invalid_coordinates}
    end
  end
end
