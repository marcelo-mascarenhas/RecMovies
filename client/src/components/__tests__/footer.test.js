import renderer from 'react-test-renderer';

import Footer from '../footer'

it('renderFooter', () => {

    const component = renderer.create(
        <Footer/>
    )
    let tree = component.toJSON();
    expect(tree).toMatchSnapshot();
  
})