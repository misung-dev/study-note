import React from "react";
import "./Square.css";

const Square = ({ onClick, value }) => {
	return (
		<button className="square" onClick={onClick}>
			{value}
		</button> // 어떤 것을 기억해야 할때는 state를 이용
	);
};

export default Square;
