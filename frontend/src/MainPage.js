import React from 'react';
import CardWithExpenses from './components/mainpage/CardWithExpenses';
import axios from 'axios';
import History from './History';
import NavBarComponent from './NavBarComponent';
import AddNewExpanse from './AddNewExpanse';

class MainPage extends React.Component {
    constructor() {
        super();
        this.state = {
            expenseData: [],
            inputExpanse: ''
        }

        this.createHistoryEl = this.createHistoryEl.bind(this);
        this.onInputChange = this.onInputChange.bind(this);
        this.getDate = this.getDate.bind(this);
    }

    onInputChange(e) {
        let newExpansesEl = parseInt(e.target.value);
        this.setState({ inputExpanse: newExpansesEl });
    }

    createHistoryEl(e) {
        e.preventDefault();

        this.setState({
            expenseData: [...this.state.expenseData, { member: 'Ala', amount: this.state.inputExpanse, date: new Date }]
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

    getDate(date) {
        var newDate = new Date(date);

        var day = newDate.getDate().toString();
        var month = newDate.getMonth().toString();
        var year = newDate.getFullYear().toString();

        return `${day.padStart(2, '0')}.${month.padStart(2, '0')}.${year.padStart(2, '0')}`;
    }



    render() {
        return (
            <div>
                <NavBarComponent />
                <div className="container-fluid mainpage" >
                    <div className="container" >
                        <div className="row">
                            <div className="col-5 content-row">
                                <h1>Expanses for room Czebotodrel</h1>
                                <div className="card-expenses">
                                    <CardWithExpenses />
                                    <CardWithExpenses />
                                </div>
                            </div>
                            <div className="col-7 content-row">
                                <h1>Your History Expanses</h1>
                                <AddNewExpanse createHistoryEl={this.createHistoryEl} onInputChange={this.onInputChange} />
                                <History expenseData={this.state.expenseData} getDate={this.getDate} />
                            </div>
                        </div>
                    </div >
                </div >
            </div>

        );
    }
}



export default MainPage;
