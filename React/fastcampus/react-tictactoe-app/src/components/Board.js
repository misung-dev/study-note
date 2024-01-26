import React, { useState } from "react";
import Square from "./Square";
import "./Board.css";

const Board = () => {
	const [squares, setSquares] = useState(Array(9).fill(null));
	const [xIsNext, setXISNext] = useState(true);

	const status = `Next player: ${xIsNext ? "X" : "O"}`;

	const handleClick = (i) => {
		const newSquares = squares.slice();
		newSquares[i] = xIsNext ? "X" : "O";
		setSquares(newSquares); // setter를 이용함
		setXISNext((previousState) => !previousState);
		// setXISNext(!xIsNext); // false로 만들어서 'O'가 표시되게 함
	};

	const renderSquare = (i) => {
		return <Square value={squares[i]} onClick={() => handleClick(i)} />;
	};

	// 함수형에서는 render없이 바로 return 함
	return (
		<div>
			<div className="status">{status}</div>
			<div className="board-row">
				{renderSquare(0)}
				{renderSquare(1)}
				{renderSquare(2)}
			</div>
			<div className="board-row">
				{renderSquare(3)}
				{renderSquare(4)}
				{renderSquare(5)}
			</div>
			<div className="board-row">
				{renderSquare(6)}
				{renderSquare(7)}
				{renderSquare(8)}
			</div>
		</div>
	);
};

export default Board;
