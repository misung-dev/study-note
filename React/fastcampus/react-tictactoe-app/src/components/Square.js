import React, { Component } from "react";
import "./Square.css";

export default class Square extends Component {
	constructor(props) {
		super(props);
		this.state = {
			value: null,
		};
	}

	render() {
		return (
			<button
				className="square"
				onClick={() => {
					this.setState({ value: "X" });
				}}
			>
				{this.state.value}
			</button> // 어떤 것을 기억해야 할때는 state를 사용
		);
	}
}
