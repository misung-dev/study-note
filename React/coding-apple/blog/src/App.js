import logo from "./logo.svg";
import "./App.css";
import { useState } from "react";

function App() {
	let post = "Contents";
	let [글제목, 글제목변경] = useState(["남자 코트 추천", "강남 우동 맛집", "파이썬 독학"]);
	let [따봉, 따봉변경] = useState([0, 0, 0]);
	let [modal, setModal] = useState(false);
	let [title, setTitle] = useState(0);
	let [입력값, 입력값변경] = useState("");

	return (
		<div className="App">
			<div className="black-nav">
				<h4 style={{ fontSize: "16px" }}>ReactBlog</h4>
			</div>
			<h4>{post}</h4>
			{/* array, object state 변경하는 법 */}
			<button
				onClick={() => {
					let copy = [...글제목];
					copy.sort();
					글제목변경(copy);
				}}
			>
				가나다순정렬
			</button>
			<button
				onClick={() => {
					let copy = [...글제목];
					copy[0] = "여자코트 추천";
					글제목변경(copy);
				}}
			>
				글수정
			</button>

			{글제목.map(function (a, i) {
				return (
					<div className="list" key={i}>
						<h4
							onClick={() => {
								setModal(true);
								setTitle(i);
							}}
						>
							{글제목[i]}
							<span
								onClick={() => {
									let copy = [...따봉];
									copy[i] = copy[i] + 1;
									따봉변경(copy);
								}}
							>
								👍
							</span>
							{따봉[i]}
						</h4>
						<p>2월 17일 발행</p>
					</div>
				);
			})}

			<input
				onChange={(e) => {
					입력값변경(e.target.value);
				}}
			/>
			<button>입력</button>

			{modal == true ? <Modal title={title} 글제목변경={글제목변경} 글제목={글제목} /> : null}
		</div>
	);
}

function Modal(props) {
	return (
		<div className="modal" style={{ background: props.color }}>
			<h4>{props.글제목[props.title]}</h4>
			<p>날짜</p>
			<p>상세내용</p>
			<button>글수정</button>
		</div>
	);
}

export default App;
