//
//  Dog+CoreDataProperties.swift
//  myDogs
//
//  Created by Akash Jagannathan on 4/1/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import Foundation
import CoreData


extension Dog {

    @nonobjc public class func fetchRequest() -> NSFetchRequest<Dog> {
        return NSFetchRequest<Dog>(entityName: "Dog");
    }

    @NSManaged public var color: String?
    @NSManaged public var name: String?
    @NSManaged public var treat: String?
    @NSManaged public var image: NSData?

}
