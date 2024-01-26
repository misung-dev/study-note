import React, { Component } from "react";
import "./Square.css";

export default class Square extends Component {
	render() {
		return (
			<button
				className="square"
				onClick={() => {
					this.props.onClick(); // state 변경하기
				}}
			>
				{this.props.value}
			</button> // 어떤 것을 기억해야 할때는 state를 이용
		);
	}
}
