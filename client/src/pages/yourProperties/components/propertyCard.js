import './propertyCard.css';

import arrow_white from '../../../assets/svg/your-properties/arrow-white.svg';
import farm_icon from '../../../assets/svg/your-properties/farm-icon.svg';

function PropertyCard({ name, location, onClick }) {
  return (
    <div className="property-card" onClick={onClick}>

      <div className="property-body">
        <div className="arrow-button">
          <div className="button">
            <img src={arrow_white} alt="Arrow"/>
          </div>
        </div>

        <div className="property-info">
          <img src={farm_icon} alt="Farm icon" className="farm-icon"/>
          <p className="farm-name">{name}</p>
          <p className="farm-location">{location}</p>
        </div>
      </div>

    </div>
  )
}

export default PropertyCard;