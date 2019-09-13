require_relative "test_helper"

xdescribe "heapsort" do
  it "sorts an empty array" do
    # Arrange 
    list = []

    # Act
    result = heapsort(list)

    # Assert
    expect(result).must_equal []
  end

  it "can sort a 1-element array" do
    # Arrange 
    list = [5]

    # Act
    result = heapsort(list)

    # Assert
    expect(result).must_equal [5]
  end
  
  it "can sort a 5-element array" do
    # Arrange 
    list = [5, 27, 3, 16, -50]

    # Act
    result = heapsort(list)

    # Assert
    expect(result).must_equal [-50, 3, 5, 16, 27]
  end  
end