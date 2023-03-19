from flask_restful import Resource, reqparse, abort
from flask import jsonify, Response
from data import db_session
from data.days import Days
from sqlalchemy import func


class DaysResource(Resource):
    def __init__(self) -> None:
        """Create sqldb parser"""
        self.parser = reqparse.RequestParser()
        self.session = db_session.create_session()
        self.parser.add_argument('day', required=False)
        self.parser.add_argument('sh', required=False)
        self.parser.add_argument('power_to_engine', required=False)
        self.parser.add_argument('temperature', required=False)
        self.parser.add_argument('oxygen', required=False)
        self.parser.add_argument('fuel', required=False)
        self.parser.add_argument('weight', required=False)
        self.parser.add_argument('distance_to_next_point', required=False)
        self.parser.add_argument('energy', required=False)

    def abort_days_not_found(self, index: int) -> None:
        """Returns 404 ERROR if id not found"""
        days = self.session.query(Days).get(index)
        if not days:
            abort(404, messsage="Day wasn't found")

    def get(self, day_id: int) -> Response:
        """API method get"""
        self.abort_days_not_found(day_id)
        day = self.session.query(Days).get(day_id)
        return jsonify({'days': day.to_dict(rules=("-day", "-day"))})

    def delete(self, day_id: int) -> Response:
        """API method delete"""
        self.abort_days_not_found(day_id)
        days = self.session.query(day_id).get(day_id)
        self.session.delete(days)
        self.session.commit()
        return jsonify({'success': 'OK'})

    def put(self, day_id: int) -> Response:
        self.abort_days_not_found(day_id)
        args = self.parser.parse_args()
        day = self.session.query(Days).get(day_id)

        match args['type']:
            case 'update_sh':
                setattr(day, 'sh', ','.join(
                    [item for item in day.sh.split(',') + [args['sh']] if item]))
            case 'update_power_to_engine':
                setattr(day, 'power_to_engine', ','.join(
                    [item for item in day.power_to_engine.split(',') + [args['power_to_engine']] if item]))
            case 'update_temperature':
                setattr(day, 'temperature', ','.join(
                    [item for item in day.temperature.split(',') + [args['temperature']] if item]))
            case 'update_oxygen':
                setattr(day, 'oxygen', ','.join(
                    [item for item in day.oxygen.split(',') + [args['oxygen']] if item]))
            case 'update_fuel':
                setattr(day, 'fuel', ','.join(
                    [item for item in day.fuel.split(',') + [args['fuel']] if item]))
            case 'update_weight':
                setattr(day, 'weight', ','.join(
                    [item for item in day.weight.split(',') + [args['weight']] if item]))
            case 'distance_to_next_point':
                setattr(day, 'distance_to_next_point', ','.join(
                    [item for item in day.distance_to_next_point.split(',') + [args['distance_to_next_point']] if item]))
            case 'update_energy':
                setattr(day, 'energy', ','.join(
                    [item for item in day.energy.split(',') + [args['energy']] if item]))

        self.session.commit()
        return jsonify({'success': 'OK'})


class DaysListResource(Resource):
    def __init__(self) -> None:
        """Create sqldb parser"""
        self.session = db_session.create_session()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('day', required=False)
        self.parser.add_argument('sh', required=False)
        self.parser.add_argument('power_to_engine', required=False)
        self.parser.add_argument('temperature', required=True)
        self.parser.add_argument('oxygen', required=False)
        self.parser.add_argument('fuel', required=False)
        self.parser.add_argument('weight', required=False)
        self.parser.add_argument('distance_to_next_point', required=False)
        self.parser.add_argument('energy', required=False)

    def get(self) -> Response:
        """API method get"""
        args = self.parser.parse_args()
        result = jsonify({'status': 'Failed'})
        match args['type']:
            case 'all':
                all_days = self.session.query(Days).all()
                result = jsonify({'days': [item.to_dict(only=('day', 'id', 'energy', 'distance_to_next_point', 'weight', 'fuel', 'oxygen', 'temperature', 'power_to_engine', 'sh')) for item in all_days]})

        return result

    def post(self) -> Response:
        """API method post"""
        args = self.parser.parse_args()
        days = Days(
            day=args['day'],
            sh=args['sh'],
            power_to_engine=args['power_to_engine'],
            temperature=args['temperature'],
            oxygen=args['oxygen'],
            weight=args['weight'],
            distance_to_next_point=args['distance_to_next_point'],
            energy=args['energy']

        )
        self.session.add(days)
        self.session.commit()
        return jsonify({'success': 'OK'})
