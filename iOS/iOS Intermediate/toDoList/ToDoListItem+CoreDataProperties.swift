//
//  ToDoListItem+CoreDataProperties.swift
//  toDoList
//
//  Created by Akash Jagannathan on 3/23/17.
//  Copyright © 2017 Akash Jagannathan. All rights reserved.
//

import Foundation
import CoreData


extension ToDoListItem {

    @nonobjc public class func fetchRequest() -> NSFetchRequest<ToDoListItem> {
        return NSFetchRequest<ToDoListItem>(entityName: "ToDoListItem");
    }

    @NSManaged public var title: String?
    @NSManaged public var itemDescription: String?
    @NSManaged public var completionDate: NSDate?

}
