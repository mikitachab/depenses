import React from 'react';
import { Card, Button } from 'react-bootstrap';

class CardWithExpenses extends React.Component {

    render() {
        return (

            <Card className="card-item" style={{ width: '18rem' }}>
                <Card.Body>
                    <Card.Title>Irina</Card.Title>
                    <Card.Text className="price">
                        50$
                    </Card.Text>
                    <Button variant="primary">Go somewhere</Button>
                </Card.Body>
            </Card>
        )
    }

}



export default CardWithExpenses;
