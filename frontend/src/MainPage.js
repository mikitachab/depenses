import React from 'react';
import './App.css';
import CardWithExpenses from './components/mainpage/CardWithExpenses';
import HistoryItem from './components/mainpage/HistoryItem';
import axios from 'axios'

class MainPage extends React.Component {
    constructor() {
        super();
        this.state = {
            expenseData: [],
            inputExpanse: ''
        }

        this.createHistoryEl = this.createHistoryEl.bind(this);
        this.onInputChange = this.onInputChange.bind(this);
        this.getCurrentDate = this.getCurrentDate.bind(this)
    }

    onInputChange(e) {
        let newExpansesEl = parseInt(e.target.value);
        this.setState({ inputExpanse: newExpansesEl });
    }

    createHistoryEl(e) {
        e.preventDefault();

        this.setState({
            expenseData: [...this.state.expenseData, { member: 'Ala', amount: this.state.inputExpanse, date: this.getCurrentDate() }]
        })

        axios.post(`http://127.0.0.1:8000/api/v1/spendings/`,
            {
                amount: this.state.inputExpanse,
                title: 'test-title',
                room: 1,
                member: 1
            },
            {
                headers: {
                    Authorization: 'Token 4c6c769ed8d5c0242e4bd63c201eedfa427c5a02'
                }
            }
        ).then(data => console.log(data));
    }

    async componentDidMount() {
        const response = await axios.get(`http://127.0.0.1:8000/api/v1/spendings/`,
            {
                headers: {
                    Authorization: 'Token 4c6c769ed8d5c0242e4bd63c201eedfa427c5a02'
                }
            });

        this.setState({
            expenseData: response.data
        })
    }

    getCurrentDate() {
        let newDate = new Date();
        let date = newDate.getDate();
        let month = newDate.getMonth();
        let year = newDate.getFullYear();

        return `${date > 10 ? `${date}` : `0${date}`}.${month > 10 ? `${month}` : `0${month}`}.${year}`
    }


    render() {
        return (
            <div className="container-fluid" >
                <div className="container mainpage" >
                    <div className="row">
                        <div className="col-4">
                            <div className="card-expenses">
                                <CardWithExpenses />
                                <CardWithExpenses />
                            </div>
                        </div>
                        <div className="col-8">
                            <div className="add-new-expense">
                                <form className="text-center" action="#!" onSubmit={this.createHistoryEl}>
                                    <input className="form-control" onChange={this.onInputChange} type="number" id="input-to-add-expenses" />
                                    <button className="add-btn btn btn-dark my-2">Add</button>
                                </form>
                            </div>
                            <div className="history">
                                {this.state.expenseData.map((el, i) => {
                                    return <HistoryItem name={el.member}
                                        key={i}
                                        price={el.amount}
                                        dateDetails={el.date} />
                                })}
                            </div>
                        </div>
                    </div>
                </div >
            </div >

        );
    }
}



export default MainPage;
